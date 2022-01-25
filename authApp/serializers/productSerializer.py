from rest_framework import serializers
from authApp.models.productModel import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "brand", "sellPrice", "packaging", "volume", "weight", "status"]

    def to_representation(self, obj):
        productRepresentation = Product.objects.get(id=obj.id)

        return {
            "id": productRepresentation.id,
            "name": productRepresentation.name, 
            "description": productRepresentation.description, 
            "category": productRepresentation.category, 
            "brand": productRepresentation.brand, 
            "sellPrice": productRepresentation.sellPrice, 
            "packaging": productRepresentation.packaging, 
            "volume": productRepresentation.volume, 
            "weight": productRepresentation.weight, 
            "status": productRepresentation.status,
        }


