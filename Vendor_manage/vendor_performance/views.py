from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from purchase_order.views import PurchaseOrderListCreateAPIView
from vendor_profile.models import vendor_profile
from .serializers import HistoricalPerformaceSerializer
from .models import HistoricalPerformance
from .utils import calculate_average_response_time,calculate_fulfillment_rate,calculate_on_time_delivery_rate,calculate_quality_rating_avg

class PerformanceCreateView(APIView):
    def get(self, request, pk):
        try:
            vendor = vendor_profile.objects.get(id=pk)
            performance = PurchaseOrderListCreateAPIView.objects.get(vendor=vendor)
            serializer = HistoricalPerformaceSerializer(performance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except vendor_profile.DoesNotExist:
            return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except vendor_profile.DoesNotExist:
            return Response({'error': 'Performance metrics not found for this vendor'}, status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request, *args, **kwargs):
        try:
            vendor_id = kwargs.get('pk')
            vendor = PurchaseOrderListCreateAPIView.objects.get(id=vendor_id)

            # Calculate performance metrics (replace with your actual calculation logic)
            on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
            quality_rating_avg = calculate_quality_rating_avg(vendor)
            average_response_time = calculate_average_response_time(vendor)
            fulfillment_rate = calculate_fulfillment_rate(vendor)

            # Create or update performance object
            performance, created = HistoricalPerformance.objects.get_or_create(vendor=vendor)
            performance.on_time_delivery_rate = on_time_delivery_rate
            performance.quality_rating_avg = quality_rating_avg
            performance.average_response_time = average_response_time
            performance.fulfillment_rate = fulfillment_rate
            performance.save()

            return Response({'message': 'Performance data saved successfully'}, status=status.HTTP_201_CREATED)
        except vendor_profile.DoesNotExist:
            return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)