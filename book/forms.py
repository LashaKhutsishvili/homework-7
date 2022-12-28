from django import forms

class CreateBookForm (forms.Form):
    name = forms.CharField(label="Book Name", max_length=100)
    author = forms.CharField(label="Author", max_length=100)