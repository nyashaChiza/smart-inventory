from inventory.models import StockMovement
from django.db.models import Sum, Count
from django.utils import timezone

class DashboardData:

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

            # Filter StockMovement instances for the current month
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

            # Filter StockMovement instances for the current month and workshop movements
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
    
    
    @staticmethod
    def get_movement_type_data():
        # Aggregate total price for each movement type
        prices_by_type = StockMovement.objects.values('movement_type').annotate(
            total_price=Sum('price')
        )

        # Create dictionary to store total prices per movement type
        prices_data = {}
        for entry in prices_by_type:
            prices_data[entry['movement_type']] = entry['total_price']

        return prices_data
    
    
    @staticmethod
    def get_status_data():
        # Aggregate total movements for each movement status
        movements_by_status = StockMovement.objects.values('movement_status').annotate(
            total_movements=Count('id')
        )

        # Create dictionary to store total movements per movement status
        movements_data = {}
        for entry in movements_by_status:
            movements_data[entry['movement_status']] = entry['total_movements']

        return movements_data