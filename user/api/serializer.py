from rest_framework import serializers
from user.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'dni', 'first_name', 'last_name', 'email', 'username', 'password', 'role']

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance
  
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'first_name', 'last_name', 'dni', 'role','is_active']

class UserUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name', 'last_name']

class UserUpdatePasswordSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['password']

  def update(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance

class UserBajaSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['is_active']