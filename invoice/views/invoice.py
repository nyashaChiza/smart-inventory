from django.shortcuts import get_object_or_404, render, redirect
from inventory.helpers.assessment import calculate_fraud_stats
from inventory.models import StockMovement
from invoice.forms import InvoiceForm
from invoice.models import Invoice
from invoice.forms import InvoiceItemForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import redirect

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            # Save the form to create the invoice
            form.instance.user = request.user
                
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
    
class InvoiceDetailView(DetailView):
    model= Invoice
    template_name = "invoice/details.html"
    context_object_name = 'invoice'

def create_invoice_item(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        
        if form.is_valid():
            product = form.cleaned_data['product']
            previous_quantity = product.quantity
            
            if product.quantity > form.cleaned_data['quantity']:
                product.quantity = product.quantity - form.cleaned_data['quantity']
                product.save()
                form.instance.unit_price = product.price 
                form.instance.invoice = invoice
                form.save()
                
                messages.success(request, 'Invoice created successfullly')
                StockMovement.objects.create(
                    name='Invoice Sale',
                    stock=product,
                    identifier = invoice.pk,
                    user = request.user,
                    current_quantity= product.quantity,
                    price=product.price,
                    movement_type='SALE',
                    movement_quantity=form.cleaned_data['quantity'],
                    previous_quantity= previous_quantity ,
                    description=''
                )
            else:
                messages.warning(request, f'Not Enough Stock In Inventory For {product}')
                
            return redirect(request.path)
    else:
        form = InvoiceItemForm()
    
    return render(request, 'invoice/invoice_item/create.html', {'form': form, 'invoice': invoice})

def assess_invoice(request, pk):
    # Retrieve the specific entry from the model
    invoice = get_object_or_404(Invoice, pk=pk)
    
    # Call your function to process the entry
    processed_output = calculate_fraud_stats(invoice.get_movements())
    
    # Include the processed output in the context
    context = {
        'entry': invoice,
        'movements': invoice.get_movements(),
        'output': processed_output,
    }
    
    # Render the template with the context
    return render(request, 'assessment/doc_detail.html', context)