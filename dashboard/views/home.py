from typing import Any
from django.views.generic import TemplateView
from dashboard.helpers import DashboardData
from datetime import datetime
class DashboardListView(TemplateView):   
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = DashboardData()
        year = datetime.now().year
        context = super().get_context_data(**kwargs)
        context['sales_data'] = data.get_sales_data(year)
        context['workshop_data'] = data.get_workshop_movements_data(year)
        context['movement_data'] = data.get_movement_type_data()
        context['status_data'] = data.get_status_data()
        
        return context
         


