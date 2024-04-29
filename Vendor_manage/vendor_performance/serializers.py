from rest_framework import serializers
from .models import HistoricalPerformance

class HistoricalPerformaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'