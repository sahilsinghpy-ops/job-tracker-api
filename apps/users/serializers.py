from rest_framework import serializers
from .models import User


class registerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"]
        )


class UserSerilzation(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email"]
