from rest_framework import serializers
from authApp.models.productPurchaseOrderModel import ProductPurchaseOrder
from authApp.models.purchaseOrderModel import PurchaseOrder
from authApp.models.productModel import Product

class ProductPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPurchaseOrder
        fields = ["idPurchaseOrder", "idProduct", "quantity", "unitPrice", "taxPercentage"]


    def to_representation(self, obj):
        productPurchaseOrderRepresentation = ProductPurchaseOrder.objects.get(id=obj.id)
        purchaseOrderRepresentation = PurchaseOrder.objects.get(id=obj.id)
        productRepresentation = Product.objects.get(id=obj.id)

        return {
            "id": productPurchaseOrderRepresentation.id,
            "idPurchaseOrder": purchaseOrderRepresentation.id, 
            "idProduct": productRepresentation.id, 
            "quantity": productPurchaseOrderRepresentation.quantity, 
            "unitPrice": productPurchaseOrderRepresentation.unitPrice, 
            "taxPercentage": productPurchaseOrderRepresentation.taxPercentage
        }


