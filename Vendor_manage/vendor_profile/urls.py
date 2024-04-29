# urls.py
from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
]