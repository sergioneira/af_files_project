from django import forms


class ProtectionResource(form.Form):
    your_name = forms.CharField(label='Your name', max_length='100')