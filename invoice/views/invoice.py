from django.shortcuts import render, redirect
from inventory.models import StockMovement
from invoice.forms import InvoiceForm
from invoice.models import Invoice
from invoice.forms import InvoiceItemForm
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            # Save the form to create the invoice
            invoice = form.save()
            
            # Redirect to the create_invoice_item view with the invoice id in the URL
            return redirect('create_invoice_item', pk=invoice.pk)
    else:
        form = InvoiceForm()
    return render(request, 'invoice/create.html', {'form': form})


class InvoiceList(ListView):
    model= Invoice
    template_name = "invoice/index.html"
    context_object_name = 'invoices'

def create_invoice_item(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        
        if form.is_valid():
            product = form.cleaned_data['product']
            previous_quantity = product.quantity
            product.quantity = product.quantity - form.cleaned_data['quantity']
            product.save()
             
            form.instance.unit_price = product.price 
            form.instance.invoice = invoice
            form.save()
            
            messages.success(request, 'Invoice created successfullly')
            StockMovement.objects.create(
                name='Invoice Sale',
                stock=product,
                user = request.user,
                current_quantity= product.quantity,
                price=product.price,
                movement_type='SALE',
                movement_quantity=form.cleaned_data['quantity'],
                previous_quantity= previous_quantity ,
                description=''
            )
            return redirect('invoice_list')  
    else:
        form = InvoiceItemForm()
    
    return render(request, 'invoice/invoice_item/create.html', {'form': form, 'invoice': invoice})