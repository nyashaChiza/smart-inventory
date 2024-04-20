from django.utils import timezone
from django.db.models import Avg
from django.conf import settings
from inventory.models import StockMovement

def get_movement_assessment(movement_entry: StockMovement):
    # Initialize dictionary to store results
    users_groups = movement_entry.user.groups.all()
    user_permissions = []
    
    for group in users_groups:
        for perm in group.permissions.all():     
            user_permissions.append(perm.name)
    result = {
        'fraud_status': None,
        'quantity_within_movement_limits': None,
        'fraud_score_below_limit': None,
        'transaction_frequency': None,
        'anomalous_transaction_amounts': None,
        'pass_fail': None,
        'fraud_score': None,
        'transaction_authorised': 'Can add stock movement' in user_permissions ,
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
        result['quantity_within_movement_limits'] = True
    else:
        result['quantity_within_movement_limits'] = False
    
    # 3. Consider existing movements and their statuses
    # Example: Determine transaction frequency
    recent_movements = StockMovement.objects.filter(
        stock=movement_entry.stock,
        created__gte=movement_entry.created - timezone.timedelta(days=30)
    )
    transaction_frequency = recent_movements.count()
    result['transaction_frequency'] = transaction_frequency < 5
    
    # 4. Check for anomalous transaction amounts
    # Example: Compare current transaction amount with historical averages
    historical_average = recent_movements.aggregate(Avg('price'))['price__avg'] or 0
    anomaly_threshold = 1.5 * historical_average  
    if price > anomaly_threshold:
        result['anomalous_transaction_amounts'] = False
    else:
        result['anomalous_transaction_amounts'] = True
    
    # Determine Pass/Fail status based on predefined criteria
    if (result['quantity_within_movement_limits'] == True and
        result['anomalous_transaction_amounts'] == True and
        (movement_type != 'ADD' or total_cost < 1000)):
        result['pass_fail'] = True
    else:
        result['pass_fail'] = False
    
    total_weight = settings.QUANTITY_WEIGHT + settings.ANOMALY_WEIGHT + settings.TRANSACTION_FREQUENCY_WEIGHT  # Add more weights if needed
    passed_weight = 0
    if result['quantity_within_movement_limits'] == True:
        passed_weight += settings.QUANTITY_WEIGHT
    if result['anomalous_transaction_amounts'] == True:
        passed_weight += settings.ANOMALY_WEIGHT
    
    fraud_score_percentage = (passed_weight / total_weight) * 100
    result['fraud_score'] =  abs(100 - fraud_score_percentage) 
    result['fraud_status'] = result['fraud_score']< settings.FRAUD__THRESHOLD
    result['fraud_score_below_limit']  = result['fraud_score']< settings.FRAUD__THRESHOLD
   
    return result


