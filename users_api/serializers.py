from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def validate_email(self, value):
        """Verificamos que el email sea único"""
        if User.objects.filter(email=value).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        return value

    def create(self, validated_data):
        """Crea un usuario con username basado en su email si no se proporciona"""
        email = validated_data['email']
        username = email.split('@')[0]  # Extrae la parte antes del '@'

        user = User(
            username=username,
            email=email
        )
        user.set_password(validated_data['password'])  # Cifra la contraseña
        user.save()
        return user
