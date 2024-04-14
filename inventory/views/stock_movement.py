from django.db.models.query import QuerySet
from inventory.models import StockMovement, Stock
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View


class StockMovementListView(ListView):
    model = StockMovement
    template_name = 'stock_movement/index.html'
    context_object_name = 'stockmovements'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock'] = Stock.objects.get(pk =self.kwargs['pk'])
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(stock=self.kwargs['pk']).all()

class StockMovementDetailView(DetailView):
    model = StockMovement
    template_name = 'stock_movement/detail.html'
    context_object_name = 'stockmovement'

class StockMovementCreateView(CreateView):
    model = StockMovement
    template_name = 'stock_movement/create.html'
    fields = ['description', 'movement_quantity', 'current_quantity', 'movement_type', 'price', 'stock']
    success_url = reverse_lazy('stock_list')

class StockMovementUpdateView(UpdateView):
    model = StockMovement
    template_name = 'stock_movement/update.html'
    fields = ['name', 'description', 'movement_quantity', 'previous_quantity', 'current_quantity', 'movement_type', 'price', 'stock']
    success_url = reverse_lazy('stockmovement_list')

class StockMovementDeleteView(View):
    model = StockMovement
    success_url = reverse_lazy('stockmovement_list')
