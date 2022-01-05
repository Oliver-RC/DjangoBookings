from django import forms


class NewsletterSignUp(forms.Form):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()