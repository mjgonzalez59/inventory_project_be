from django.http import request, response
from rest_framework import generics, serializers, status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authApp.serializers.clientSerializer import ClientSerializer

class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Cliente creado", status=status.HTTP_201_CREATED)


from authApp.models.clientModel import Client


class ClientDetailView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    permission_class = (IsAuthenticated, )
    queryset = Client.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ClientByCC(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        ccClient = kwargs["pk"]
        try:
            query = Client.objects.filter(status="Active").get(cc=ccClient)
            clientData = {
                "id": query.id,
                "cc": query.cc,
                "name": query.name,
                "address": query.address,
                "phone": query.phone,
                "email": query.email,
                "country": query.country,
                "contactName": query.contactName,
                "status": query.status,
            }
            return  Response(clientData, status=status.HTTP_201_CREATED)
        except:
            return  Response("Cliente no encontrado en la base de datos", status=status.HTTP_404_NOT_FOUND)



class ClientUpdateView(generics.UpdateAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Client.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ClientDeleteView(generics.DestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Client.objects.all()

    def get(self, request, *args, **kwargs):
        Client.objects.filter(id=kwargs['pk']).update(status='Inactive')
        return Response("Cliente eliminado", status=status.HTTP_201_CREATED)



class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Client.objects.filter(status="Active")
        return queryset



