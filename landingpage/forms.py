from django import forms
from rieltor_object.models import TypeDeal


class LandingForms(forms.Form):
    type_deal = forms.MultipleChoiceField(choices=TypeDeal.CHOICES)
    price__gt = forms.IntegerField()
    price__lt = forms.IntegerField()
    footage__gt = forms.IntegerField()
    footage__lt = forms.IntegerField()
