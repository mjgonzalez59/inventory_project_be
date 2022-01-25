from rest_framework import serializers
from authApp.models.purchaseOrderModel import PurchaseOrder
from authApp.models.userModel import User
from authApp.models.supplierModel import Supplier


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["createdByUserId", "idSupplier", "paymentMethod", "date", "status"]

    def to_representation(self, obj):
        purchaseOrderRepresentation = PurchaseOrder.objects.get(id=obj.id)
        userRepresentation = User.objects.get(id=obj.id)
        supplierRepresentation = Supplier.objects.get(id=obj.id)

        return {
            "id": purchaseOrderRepresentation.id,
            "createdByUserId": userRepresentation.id, 
            "idSupplier": supplierRepresentation.id, 
            "paymentMethod": purchaseOrderRepresentation.paymentMethod, 
            "date": purchaseOrderRepresentation.date, 
            "status": purchaseOrderRepresentation.status
        }

