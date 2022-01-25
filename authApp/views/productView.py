from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authApp.serializers.productSerializer import ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Producto creado", status=status.HTTP_201_CREATED)


from authApp.models.productModel import Product

class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class ProductByName(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        nameInput = self.kwargs["pk"]
        try:
            queryset = Product.objects.filter(name=nameInput)
            print(queryset)
            return  queryset
        except:
            return  Response("Producto no encontrado en la base de datos", status=status.HTTP_404_NOT_FOUND)




class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)



class ProductDeleteView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        Product.objects.filter(id=kwargs['pk']).update(status='Inactive')
        return Response("Producto eliminado", status=status.HTTP_201_CREATED)


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Product.objects.filter(status="Active")
        return queryset