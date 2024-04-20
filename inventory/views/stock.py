from inventory.models import Stock
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from inventory.forms import StockMovementForm
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, redirect
from inventory.models.stock_movements import StockMovement
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View



def add_stock_movements(request, pk, **kwargs):
    stock = get_object_or_404(Stock, pk=pk)
    
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            movement_quantity = form.cleaned_data['movement_quantity']
            movement_type = form.cleaned_data['movement_type']
            description = form.cleaned_data['description']
            
            current_quantity = stock.quantity 
            price = stock.price
            if movement_type != 'ADD':
                if stock.quantity < movement_quantity:
                    messages.warning(request, f'Not enough stock in {stock}')
                    return redirect('stock_list')
                stock.quantity = stock.quantity - movement_quantity
                stock.save()
            elif movement_type == 'ADD':
                stock.quantity = stock.quantity + movement_quantity
                stock.save()
            else:
                messages.warning(request, f'Invalid movement type: {movement_type}')
                return redirect('stock_list')
                
            StockMovement.objects.create(
                name='Direct Inventory',
                stock=stock,
                user = request.user,
                current_quantity= stock.quantity,
                price=price,
                movement_type=movement_type,
                movement_quantity=movement_quantity,
                previous_quantity= current_quantity ,
                description=description
            )
            
            messages.success(request, f'Movement added to {stock} successfully')
            return redirect('stock_list')
        else:
            messages.warning(request, form.errors)
    
class StockListView(ListView):
    model = Stock
    template_name = 'stock/index.html'
    context_object_name = 'stocks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movement_form'] = StockMovementForm()
        return context
    

class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock/detail.html'
    context_object_name = 'stock'

class StockCreateView(SuccessMessageMixin ,CreateView):
    model = Stock
    template_name = 'stock/create.html'
    fields = ['name', 'description', 'quantity', 'price', 'category']
    success_message = "Stock created successfully"
    success_url = reverse_lazy('stock_list')


class StockUpdateView(SuccessMessageMixin, UpdateView):
    model = Stock
    template_name = 'stock/update.html'
    fields = ['name', 'description', 'quantity', 'price', 'category']
    success_message = "Stock updated successfully"
    success_url = reverse_lazy('stock_list')

    def form_valid(self, form):
        # Save the form with proper error handling
        try:
            self.object = form.save()
            return super().form_valid(form)
        except Exception as e:
            messages.warning(self.request, f"An error occurred: {str(e)}:{form.error}")
            return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        # Display form errors to the user
        messages.warning(self.request, f"Form submission failed. Please correct the errors. {form.errors}")
        return super().form_invalid(form)



class StockDeleteView(View):
    model = Stock
    success_url = reverse_lazy('stock_list')
