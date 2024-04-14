
from inventory.models import StockMovement


def get_movement_assessment(movement: StockMovement):
    
    return {
        'fraud_score': 89,
        'description': 'test description',
        'status': 'test status',
    }