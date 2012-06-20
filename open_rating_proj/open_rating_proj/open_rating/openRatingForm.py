from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

class openRatingForm(forms.Form):
    defautExterieur=forms.ChoiceField(widget=RadioSelect,choices=['oui','non'])
    
    dettePib = forms.CharField(max_length=3)
    deficitPib=forms.CharField(max_length=3)

    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
