from django.http import response
from rest_framework import serializers, status, views
import rest_framework
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "username":request.data["username"],
            "password":request.data["password"]
        }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


from django.conf import settings
from rest_framework import generics, status
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.userModel import User


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Acceso no autorizado - Información detallada de Usuario'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)





class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Acceso no autorizado - Actualización de Usuario'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)




class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        User.objects.filter(id=kwargs['pk']).update(status='updating')
        return Response("User eliminado", status=status.HTTP_201_CREATED)




class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

