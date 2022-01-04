from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'please enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'please enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@email.com'}),
            'phone': forms.NumberInput(attrs={'placeholder': '01234567890'}),
            'requirements': forms.TextInput(attrs={'placeholder': 'please list any booking requirements e.g. highchair, dietary requirements, access needs etc.'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }