from rest_framework import serializers
from django.db.models import fields
from .models import User, Translation
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Id', 'Name', 'QuotaLimit', 'QuotaSpent']

class TranslationSerializer(serializers.ModelSerializer):
    #FromUserId = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Translation
        fields = ('Id', 'InputText', 'OutputText', 'FromUserId')