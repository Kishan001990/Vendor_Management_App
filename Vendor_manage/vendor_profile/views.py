
# views.py
from rest_framework import generics
from .models import vendor_profile
from .serializers import VendorSerializer


 # API view for 
class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = vendor_profile.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = vendor_profile.objects.all()
    serializer_class = VendorSerializer