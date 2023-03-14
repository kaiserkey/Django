from django import forms

class CreateNewTask():
    title = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(label="Content", max_length=200)
    due_date = forms.DateField(label="Due date")
    priority = forms.CharField(label="Priority", max_length=200)