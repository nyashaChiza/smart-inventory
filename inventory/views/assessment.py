
from django.contrib import messages
from django.shortcuts import  get_object_or_404, redirect
from inventory.forms import AssessmentForm
from inventory.models import StockMovement
from inventory.forms import AssessmentForm
from django.views.generic import ListView, DetailView
from inventory.helpers import get_movement_assessment


class MovementListView(ListView):
    model = StockMovement
    template_name = 'assessment/index.html'
    context_object_name = 'movements'
    
    
class MovementDetailView(DetailView):
    model = StockMovement
    template_name = 'assessment/detail.html'
    context_object_name = 'movement'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assessment'] = get_movement_assessment(self.object)
        context['assessment_form'] = AssessmentForm()
        return context
    

def assessment_view(request, pk):
    movement = get_object_or_404(StockMovement, pk=pk)

    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            messages.info(request, 'Assessment saved successfully')
            
    else:
        form = AssessmentForm(instance=movement)
    
    return  redirect('assessment_list')
