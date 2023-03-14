from django import forms

class CreateNewTask():
    title = forms.CharField(label="Titulo de la tarea", max_length=200)
    description = forms.Textarea(max_length=200)