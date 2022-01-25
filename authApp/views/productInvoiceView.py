from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authApp.serializers.productInvoiceSerializer import ProductInvoiceSerializer

class ProductInvoiceCreateView(generics.CreateAPIView):
    serializer_class = ProductInvoiceSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = ProductInvoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("ProductInvoice Creado", status=status.HTTP_201_CREATED)



from authApp.models.productInvoiceModel import ProductInvoice


class ProductInvoiceDetailView(generics.RetrieveAPIView):
    serializer_class = ProductInvoiceSerializer
    permission_classes = (IsAuthenticated, )
    queryset = ProductInvoice.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




class ProductInvoiceUpdateView(generics.UpdateAPIView):
    serializer_class = ProductInvoiceSerializer
    permission_classes = (IsAuthenticated, )
    queryset = ProductInvoice.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)




