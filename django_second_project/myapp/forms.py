from django import forms

class CreateNewTask():
    title = forms.CharField(label="Title", max_length=200)
    description = 