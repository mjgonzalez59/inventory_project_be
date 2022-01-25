from rest_framework import serializers
from authApp.models.supplierModel import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'companyId', 'address', 'phone', 'email', 'country', 'contactName', 'status']


    def to_representation(self, obj):
        supplierRepresentation = Supplier.objects.get(id=obj.id)

        return {
            "id": supplierRepresentation.id,
            "name": supplierRepresentation.name,
            "companyId": supplierRepresentation.companyId,
            "address": supplierRepresentation.address,
            "phone": supplierRepresentation.phone,
            "email": supplierRepresentation.email,
            "country": supplierRepresentation.country,
            "contactName": supplierRepresentation.contactName,
            "status": supplierRepresentation.status,
        }

