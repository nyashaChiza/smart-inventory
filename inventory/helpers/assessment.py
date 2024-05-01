from django.utils import timezone
from django.db.models import Avg
from django.conf import settings
import random as rm
from inventory.models import StockMovement

def get_movement_assessment(movement_entry: StockMovement):
    # Initialize dictionary to store results
    users_groups = movement_entry.user.groups.all()
    user_permissions = [perm.name for group in users_groups for perm in group.permissions.all()]
    
    result = {
        'fraud_status': None,
        'quantity_within_movement_limits': None,
        'fraud_score_below_limit': None,
        'transaction_frequency': None,
        'anomalous_transaction_amounts': None,
        'pass_fail': None,
        'fraud_score': None,
        'transaction_authorised': 'Can add stock movement' in user_permissions,
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
    if 1 < quantity <= rm.randint(10,15):  # Define your movement limits
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
    if (result['quantity_within_movement_limits'] and
        result['anomalous_transaction_amounts'] and
        (movement_type != 'ADD' or total_cost < 1000)):
        result['pass_fail'] = True
    else:
        result['pass_fail'] = False
    
    total_weight = settings.QUANTITY_WEIGHT + settings.ANOMALY_WEIGHT + settings.TRANSACTION_FREQUENCY_WEIGHT  # Add more weights if needed
    passed_weight = 0
    if result['quantity_within_movement_limits']:
        passed_weight += settings.QUANTITY_WEIGHT
    if result['anomalous_transaction_amounts']:
        passed_weight += settings.ANOMALY_WEIGHT
    
    fraud_score_percentage = (passed_weight / total_weight) * 100
    result['fraud_score'] =  abs(100 - fraud_score_percentage) + rm.randrange(-7,9)
    result['fraud_status'] = result['fraud_score'] < settings.FRAUD_THRESHOLD
    result['fraud_score_below_limit']  = result['fraud_score'] < settings.FRAUD_THRESHOLD
   
    return result

def calculate_fraud_stats(stock_movements):
    total_movements = len(stock_movements) if len(stock_movements) > 0 else 1 
    total_clean_movements = sum(1 for movement in stock_movements if movement.movement_status == 'Approved')/total_movements * 100
    total_pending_movements = sum(1 for movement in stock_movements if movement.movement_status == 'Pending')/total_movements * 100
    total_flagged_movements = sum(1 for movement in stock_movements if movement.movement_status == 'Flagged')/total_movements * 100
    total_fraud_score = sum(get_movement_assessment(movement)['fraud_score'] for movement in stock_movements if movement.movement_status == 'Flagged')

    average_fraud_score = total_fraud_score / total_flagged_movements if total_flagged_movements > 0 else 0

    # Calculate the percentage of flagged movements
    flagged_percentage = (total_flagged_movements / total_movements) * 100 if total_movements > 0 else 0

    # Determine overall assessment based on predefined thresholds or criteria
    overall_assessment = ''
    if total_flagged_movements == 0:
        overall_assessment = 'Low Risk'
    elif average_fraud_score <= 5:
        overall_assessment = 'Medium Risk'
    else:
        overall_assessment = 'High Risk'

    return {
        'total_clean_movements': total_clean_movements,
        'total_flagged_movements': total_flagged_movements,
        'average_fraud_score': average_fraud_score,
        'flagged_percentage': flagged_percentage,
        'overall_assessment': overall_assessment,
        'total_pending_movements':total_pending_movements,
    }
