from django.urls import path
from .views import HistoricalPerformanceListCreateAPIView

urlpatterns = [
    path('api/vendors/<int:pk>/performance', HistoricalPerformanceListCreateAPIView.as_view(), name='purchase-order-list-create')
]