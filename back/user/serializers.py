from rest_framework import serializers
from .models import UserCustomer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomer
        fields ="__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserCustomer.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
