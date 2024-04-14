
from inventory.models import StockMovement
from django.conf import settings

def get_movement_assessment(movement: StockMovement):
    fraud_score = 68
    return {
        'fraud_score': fraud_score,
        'description': 'test description',
        'status': True,
        'within_limits': True,
        'fraud_score_threshold_status': fraud_score<settings.FRAUD_SCORE_THRESHOLD ,
    }