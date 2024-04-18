from django.utils import timezone
from django.db.models import Avg
from django.conf import settings
from inventory.models import StockMovement

def get_movement_assessment(movement_entry: StockMovement):
    # Initialize dictionary to store results
    result = {
        'Fraud Status': None,
        'Quantity Within Movement Limits': None,
        'Fraud Score Below Limit': None,
        'Transaction Frequency': None,
        'Anomalous Transaction Amounts': None,
        'Pass/Fail': None,
        'Fraud Score': None  # New field for fraud score
    }
    
    # Perform analysis based on movement entry
    
    # 1. Calculate values required for fraud detection
    quantity = movement_entry.movement_quantity
    price = movement_entry.price
    movement_type = movement_entry.movement_type
    
    # Example: Calculate total cost
    total_cost = price * quantity
    
    # 2. Compare values against thresholds or limits
    # Example: Determine if quantity is within movement limits
    if 0 < quantity <= 100:  # Define your movement limits
        result['Quantity Within Movement Limits'] = 'passed'
    else:
        result['Quantity Within Movement Limits'] = 'failed'
    
    # 3. Consider existing movements and their statuses
    # Example: Determine transaction frequency
    recent_movements = StockMovement.objects.filter(
        stock=movement_entry.stock,
        created__gte=movement_entry.created - timezone.timedelta(days=30)
    )
    transaction_frequency = recent_movements.count()
    result['Transaction Frequency'] = transaction_frequency
    
    # 4. Check for anomalous transaction amounts
    # Example: Compare current transaction amount with historical averages
    historical_average = recent_movements.aggregate(Avg('price'))['price__avg'] or 0
    anomaly_threshold = 1.5 * historical_average  
    if price > anomaly_threshold:
        result['Anomalous Transaction Amounts'] = 'failed'
    else:
        result['Anomalous Transaction Amounts'] = 'passed'
    
    # Determine Pass/Fail status based on predefined criteria
    if (result['Quantity Within Movement Limits'] == 'passed' and
        result['Anomalous Transaction Amounts'] == 'passed' and
        # Add more conditions based on your criteria
        # Example: Fraud status based on movement type
        (movement_type != 'ADD' or total_cost < 1000)):
        result['Pass/Fail'] = 'Pass'
    else:
        result['Pass/Fail'] = 'Fail'
    
    # Calculate fraud score based on weights assigned to each indicator
    total_weight = settings.QUANTITY_WEIGHT + settings.ANOMALY_WEIGHT + settings.TRANSACTION_FREQUENCY_WEIGHT  # Add more weights if needed
    passed_weight = 0
    if result['Quantity Within Movement Limits'] == 'passed':
        passed_weight += settings.QUANTITY_WEIGHT
    if result['Anomalous Transaction Amounts'] == 'passed':
        passed_weight += settings.ANOMALY_WEIGHT
    # Add weights for other indicators as needed
    # Calculate fraud score as a percentage of the total weight
    fraud_score_percentage = (passed_weight / total_weight) * 100
    result['Fraud Score'] =  fraud_score_percentage
    result['fraud Status'] = result['Fraud Score']< settings.FRAUD__THRESHOLD
    
    return result
