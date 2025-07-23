from django import forms
from .models import Emp

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your email", max_length=100,required=True)
    name=forms.CharField(label="Enter Your name", max_length=100)
    feedback=forms.CharField(label="Your feedback",widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name', 'emp_id', 'emp_email', 'phone', 'address', 'working','department']