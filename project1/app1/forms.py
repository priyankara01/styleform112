from django import forms
from django.utils.safestring import mark_safe


class StudentForm(forms.Form):
    roll = forms.IntegerField(label=mark_safe(''), widget=forms.NumberInput(attrs={'placeholder': 'Enter Roll No.'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Address'}))
    mail = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Mail ID'}))
    phone_no = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Enter Mobile No.'}))
    Date = forms.DateField(label='', widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter Date'}))
