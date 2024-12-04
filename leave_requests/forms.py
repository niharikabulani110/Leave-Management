from django import forms
from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason'] 