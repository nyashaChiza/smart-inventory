from django import forms
from job_card.models import JobCard

class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        fields = ['title', 'description']
