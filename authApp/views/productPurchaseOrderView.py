from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authApp.serializers.productPurchaseOrderSerializer import ProductPurchaseOrderSerializer

class ProductPurchaseOrderCreateView(generics.CreateAPIView):
    serializer_class = ProductPurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = ProductPurchaseOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("ProductPurchaseOrder Creada", status=status.HTTP_201_CREATED)


from authApp.models.productPurchaseOrderModel import ProductPurchaseOrder

class ProductPurchaseOrderDetailView(generics.RetrieveAPIView):
    serializer_class = ProductPurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )
    queryset = ProductPurchaseOrder.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class ProductPurchaseOrderUpdateView(generics.UpdateAPIView):
    serializer_class = ProductPurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )
    queryset = ProductPurchaseOrder.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


