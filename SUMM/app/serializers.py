from rest_framework import serializers
from django.db.models import fields
from .models import User
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Id', 'Name', 'QuotaLimit', 'QuotaSpent']