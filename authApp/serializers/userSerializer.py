from rest_framework import serializers
from authApp.models.userModel import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'role', 'email', 'gender', 'phone', 'country', 'status']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance


    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "name": user.name,
            "role": user.role,
            "email": user.email,
            "gender": user.gender,
            "phone": user.phone,
            "country": user.country,
            "status": user.status
        }

