from rest_framework import generics
from .models import HistoricalPerformance
from vendor_profile.models import vendor_profile
from rest_framework import status
from rest_framework.response import Response
from .serializers import HistoricalPerformaceSerializer

class HistoricalPerformanceListCreateAPIView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformaceSerializer


    def retrieve(self, request, *args, **kwargs):
        try:
            vendor_id = kwargs.get('id')
            vendor = vendor_profile.objects.get(id=vendor_id)
            performance_metrics = self.get_queryset().filter(vendor=vendor)
            if not performance_metrics.exists():
                return Response({'error': 'Performance metrics not found for this vendor'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(performance_metrics, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except vendor_profile.DoesNotExist:
            return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)

