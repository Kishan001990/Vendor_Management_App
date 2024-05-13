from django.urls import path
from .views import PerformanceCreateView

urlpatterns = [
    path('api/vendors/<int:pk>/performance/', PerformanceCreateView.as_view(), name='vendor_performance'),
]