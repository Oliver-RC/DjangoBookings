from django import forms
from .models import Newsletter


class NewsletterSignUp(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'please enter your first name'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'please enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@email.com'}),
        }
