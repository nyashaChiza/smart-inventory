from inventory.models import StockMovement
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View


class StockMovementListView(ListView):
    model = StockMovement
    template_name = 'stock_movement/list.html'
    context_object_name = 'stockmovements'

class StockMovementDetailView(DetailView):
    model = StockMovement
    template_name = 'stock_movement/detail.html'
    context_object_name = 'stockmovement'

class StockMovementCreateView(CreateView):
    model = StockMovement
    template_name = 'stock_movement/create.html'
    fields = ['name', 'description', 'movement_quantity', 'previous_quantity', 'current_quantity', 'movement_type', 'price', 'stock']
    success_url = reverse_lazy('stockmovement_list')

class StockMovementUpdateView(UpdateView):
    model = StockMovement
    template_name = 'stock_movement/update.html'
    fields = ['name', 'description', 'movement_quantity', 'previous_quantity', 'current_quantity', 'movement_type', 'price', 'stock']
    success_url = reverse_lazy('stockmovement_list')

class StockMovementDeleteView(View):
    model = StockMovement
    success_url = reverse_lazy('stockmovement_list')
