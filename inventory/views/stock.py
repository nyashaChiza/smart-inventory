from inventory.models import Stock
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View


class StockListView(ListView):
    model = Stock
    template_name = 'stock/index.html'
    context_object_name = 'stocks'

class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock/detail.html'
    context_object_name = 'stock'

class StockCreateView(CreateView):
    model = Stock
    template_name = 'stock/create.html'
    fields = ['name', 'description', 'quantity', 'price', 'category']
    success_url = reverse_lazy('stock_list')

class StockUpdateView(UpdateView):
    model = Stock
    template_name = 'stock/update.html'
    fields = ['name', 'description', 'quantity', 'price', 'category']
    success_url = reverse_lazy('stock_list')

class StockDeleteView(View):
    model = Stock
    success_url = reverse_lazy('stock_list')
