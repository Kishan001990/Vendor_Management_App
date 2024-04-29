# serializers.py
from rest_framework import serializers
from .models import vendor_profile

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_profile
        fields = '__all__'
