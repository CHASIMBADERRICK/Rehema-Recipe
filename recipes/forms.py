from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 255)
    last_name = forms.CharField(max_length = 255)
    email_address = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)