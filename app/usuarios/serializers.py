from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.password_validation import validate_password

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'rol')

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            rol=validated_data['rol']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
