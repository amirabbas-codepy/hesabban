from rest_framework import serializers
from app_TRC.models import Trancion
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        
class TrancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trancion
        fields = ['id', 'amount', 'descripition', 'date', 'code', 'status_TRC']
    