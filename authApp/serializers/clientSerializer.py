from rest_framework import serializers
from authApp.models.clientModel import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['cc', 'name', 'address', 'phone', 'email', 'country', 'contactName', 'status']


    def to_representation(self, obj):
        clientRepresentation = Client.objects.get(id=obj.id)

        return {
            "cc": clientRepresentation.cc,
            "id": clientRepresentation.id,
            "name": clientRepresentation.name,
            "address": clientRepresentation.address,
            "phone": clientRepresentation.phone,
            "email": clientRepresentation.email,
            "country": clientRepresentation.country,
            "contactName": clientRepresentation.contactName,
            "status": clientRepresentation.status,
        }

 
