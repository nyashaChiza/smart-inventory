
from inventory.models import StockMovement
from django.views.generic import ListView, DetailView
from inventory.helpers import get_movement_assessment


class MovementListView(ListView):
    model = StockMovement
    template_name = 'assessment/index.html'
    context_object_name = 'movements'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(stock=self.kwargs['pk']).all()

class MovementDetailView(DetailView):
    model = StockMovement
    template_name = 'assessment/detail.html'
    context_object_name = 'movement'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assessment'] = get_movement_assessment(self.object)



