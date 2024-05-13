from datetime import datetime
from django.db import models


def calculate_on_time_delivery_rate(vendor):
    total_completed_orders = vendor.purchase_order.filter(status='completed').count()
    if total_completed_orders == 0:
        return 0

    on_time_orders = vendor.purchase_order.filter(
        status='completed',
        delivery_date__lte=datetime.now()  # Assuming delivery_date is a DateTimeField
    ).count()

    return (on_time_orders / total_completed_orders) * 100

def calculate_quality_rating_avg(vendor):
    completed_orders = vendor.purchase_order.filter(status='completed').exclude(quality_rating__isnull=True)
    if not completed_orders.exists():
        return 0

    total_quality_ratings = completed_orders.aggregate(total=models.Sum('quality_rating'))['total']
    total_orders = completed_orders.count()

    return total_quality_ratings / total_orders

def calculate_average_response_time(vendor):
    completed_orders = vendor.purchase_order.filter(status='completed', acknowledgment_date__isnull=False)
    if not completed_orders.exists():
        return 0

    total_response_time = sum((order.acknowledgment_date - order.issue_date).days for order in completed_orders)
    total_orders = completed_orders.count()

    return total_response_time / total_orders

def calculate_fulfillment_rate(vendor):
    total_orders = vendor.purchase_order.count()
    if total_orders == 0:
        return 0

    successful_orders = vendor.purchase_order.filter(status='completed').exclude(issue_date__isnull=True)
    successful_count = successful_orders.count()

    return (successful_count / total_orders) * 100