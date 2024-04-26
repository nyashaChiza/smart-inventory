from django.shortcuts import render, redirect
from inventory.models import StockMovement
from job_card.models import JobCard
from job_card.form import JobCardForm, JobCardItemForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import redirect

def create_job_card(request):
    if request.method == 'POST':
        form = JobCardForm(request.POST)
        if form.is_valid():
            # Save the form to create the invoice
            job_card = form.save()
            
            # Redirect to the create_invoice_item view with the invoice id in the URL
            return redirect('create_job_card_item', pk=job_card.pk)
    else:
        form = JobCardForm()
    return render(request, 'job_card/create.html', {'form': form})


class JobCardList(ListView):
    model= JobCard
    template_name = "job_card/index.html"
    context_object_name = 'cards'

class JobCardDetailView(DetailView):
    model= JobCard
    template_name = "job_card/details.html"
    context_object_name = 'card'

def create_job_card_item(request, pk):
    job_card = JobCard.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = JobCardItemForm(request.POST)
        
        if form.is_valid():
            product = form.cleaned_data['stock']
            previous_quantity = product.quantity
            product.quantity = product.quantity - form.cleaned_data['quantity']
            product.save()
             
            form.instance.unit_price = product.price 
            form.instance.job_card = job_card
            form.save()
            
            messages.success(request, 'Job Card created successfullly')
            StockMovement.objects.create(
                name='Job Card Sale',
                stock=product,
                user = request.user,
                current_quantity= product.quantity,
                price=product.price,
                movement_type='SALE',
                movement_quantity=form.cleaned_data['quantity'],
                previous_quantity= previous_quantity ,
                description=''
            )
            return redirect('job_card_list')  
    else:
        form = JobCardItemForm()
    
    return render(request, 'job_card/job_card_item/create.html', {'form': form, 'job_card': job_card})