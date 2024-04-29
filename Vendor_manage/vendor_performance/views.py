from rest_framework import generics
from .models import HistoricalPerformance
from .serializers import HistoricalPerformaceSerializer

class HistoricalPerformanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformaceSerializer
