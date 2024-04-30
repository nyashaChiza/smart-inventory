from django import forms
from job_card.models import JobCard

class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        fields = ['title', 'description', 'card_type']

    def __init__(self,  *args, **kwargs):
        super(JobCardForm, self).__init__(*args, **kwargs)    
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"