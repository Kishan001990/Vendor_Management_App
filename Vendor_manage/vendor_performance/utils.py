from purchase_order.models import PurchaseOrder
from .models import HistoricalPerformance
import datetime
import models

def calculate_vendor_performance(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed')
    total_orders = vendor.purchaseorder_set.all()

    # Calculate metrics
    on_time_delivery_rate = (completed_orders.filter(delivery_date__lte=models.F('acknowledgment_date')).count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0.0
    quality_rating_avg = sum(completed_orders.exclude(quality_rating=None).values_list('quality_rating', flat=True)) / completed_orders.exclude(quality_rating=None).count() if completed_orders.exclude(quality_rating=None).count() > 0 else 0.0
    response_times = completed_orders.exclude(acknowledgment_date=None).annotate(
        response_time=models.ExpressionWrapper(models.F('acknowledgment_date') - models.F('issue_date'), output_field=models.DurationField())
    ).values_list('response_time', flat=True)
    average_response_time = sum(response_times, datetime.timedelta()) / len(response_times) if response_times else datetime.timedelta(0)
    fulfillment_rate = (completed_orders.filter(status='completed').count() / total_orders.count()) * 100 if total_orders.count() > 0 else 0.0

    # Create historical performance record
    historical_performance = HistoricalPerformance(
        vendor=vendor,
        date=datetime.datetime.now(),
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time.total_seconds() / 3600,  # Convert to hours
        fulfillment_rate=fulfillment_rate
    )
    historical_performance.save()