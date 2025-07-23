from __future__ import annotations

from django.contrib.auth import get_user_model
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
    )

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "first_name", "last_name", "username"]

    def validate(self, data):
        email = data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError("Email is already registered.")

        return data

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            username=validated_data.get(
                "username",
                validated_data["email"][:9],
            ),
        )
        return user
