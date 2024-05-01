from inventory.models import StockMovement
from django.db.models import Sum, Count
from django.utils import timezone

class DashboardData:
    def get_top_movements(self):
        top_movements = StockMovement.objects.values('stock__name').annotate(total_movements=Count('id')).order_by('-total_movements')[:5]
        top_results = [{'stock_name': movement['stock__name'], 'total_movements': movement['total_movements']} for movement in top_movements]
        return top_results

   
    def get_bottom_movements(self):
        bottom_movements = StockMovement.objects.values('stock__name').annotate(total_movements=Count('id')).order_by('total_movements')[:5]
        bottom_results = [{'stock_name': movement['stock__name'], 'total_movements': movement['total_movements']} for movement in bottom_movements]
        return bottom_results
    @staticmethod
    def get_sales_data(year: int):
        # Initialize dictionary to store total sales for each month
        total_sales_per_month = {}

        # Loop through each month of the year
        for month in range(1, 13):
            # Calculate the start and end dates of the month
            start_date = timezone.datetime(year, month, 1)
            if month == 12:
                end_date = timezone.datetime(year+1, 1, 1) - timezone.timedelta(days=1)
            else:
                end_date = timezone.datetime(year, month+1, 1) - timezone.timedelta(days=1)

            # Filter StockMovement instances for the current month and year
            sales_for_month = StockMovement.objects.filter(
                movement_type='SALE',
                created__gte=start_date,
                created__lte=end_date
            ).aggregate(
                total_sales=Sum('movement_quantity')
            )['total_sales'] or 0

            # Store the total sales for the current month
            month_abbr_name = timezone.datetime(year, month, 1).strftime('%b')  # Get month abbreviation (e.g., Jan, Feb)
            total_sales_per_month[month_abbr_name] = sales_for_month

        return total_sales_per_month

    @staticmethod
    def get_workshop_movements_data(year: int):
        # Initialize dictionary to store total movements for each month
        total_movements_per_month = {}

        # Loop through each month of the year
        for month in range(1, 13):
            # Calculate the start and end dates of the month
            start_date = timezone.datetime(year, month, 1)
            if month == 12:
                end_date = timezone.datetime(year+1, 1, 1) - timezone.timedelta(days=1)
            else:
                end_date = timezone.datetime(year, month+1, 1) - timezone.timedelta(days=1)

            # Filter StockMovement instances for the current month, year, and workshop movements
            workshop_movements_for_month = StockMovement.objects.filter(
                movement_type='USAGE',  # Filter for workshop movements
                created__gte=start_date,
                created__lte=end_date
            ).aggregate(
                total_movements=Sum('movement_quantity')
            )['total_movements'] or 0

            # Store the total movements for the current month
            month_abbr_name = timezone.datetime(year, month, 1).strftime('%b')  # Get month abbreviation (e.g., Jan, Feb)
            total_movements_per_month[month_abbr_name] = workshop_movements_for_month

        return total_movements_per_month
