from django import forms
from .models import Newsletter


class NewsletterSignUp(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'