from django import forms


class CreateReaderForm (forms.Form):
    name = forms.CharField(label="name", max_length=100)
    lastname = forms.CharField(label="lastname", max_length=100)