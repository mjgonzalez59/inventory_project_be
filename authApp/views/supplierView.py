from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authApp.serializers.supplierSerializer import SupplierSerializer

class SupplierCreateView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = SupplierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Supplier creado", status=status.HTTP_201_CREATED)


from authApp.models.supplierModel import Supplier


class SupplierDetailView(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    permission_class = (IsAuthenticated, )
    queryset = Supplier.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class SupplierBycompanyId(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        companyID = kwargs["pk"]
        try:
            query = Supplier.objects.filter(status="Active").get(companyId=companyID)
            supplierData = {
                "id": query.id,
                "name": query.name,
                "companyId": query.companyId,
                "address": query.address,
                "phone": query.phone,
                "email": query.email,
                "country": query.country,
                "contactName": query.contactName,
                "status": query.status
            }
            return  Response(supplierData, status=status.HTTP_201_CREATED)
        except:
            return  Response("Supplier no encontrado en la base de datos", status=status.HTTP_404_NOT_FOUND)





class SupplierUpdateView(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Supplier.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)




class SupplierDeleteView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Supplier.objects.all()

    def get(self, request, *args, **kwargs):
        Supplier.objects.filter(id=kwargs['pk']).update(status='Inactive')
        return Response("Supplier eliminado", status=status.HTTP_201_CREATED)



class SupplierListView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Supplier.objects.filter(status="Active")
        return queryset
