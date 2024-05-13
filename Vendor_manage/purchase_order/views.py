from rest_framework import generics
from .models import PurchaseOrder
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
from .serializers import PurchaseOrderSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class AcknowledgePurchaseOrderView(APIView):
    def post(self, request, pk):
        # Retrieve the purchase order
        purchase_order = get_object_or_404(PurchaseOrder, id=pk)
        
        # Check if the purchase order has already been acknowledged
        if purchase_order.acknowledgment_date:
            return Response({'error': 'Purchase order already acknowledged'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Update the acknowledgment date to the current timestamp
        purchase_order.acknowledgment_date = datetime.now()
        purchase_order.save()
        
        return Response({'message': 'Purchase order acknowledged successfully'}, status=status.HTTP_200_OK)