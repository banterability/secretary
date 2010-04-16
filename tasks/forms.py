from django import forms
from secretary.tasks.models import Task


class TaskForm(forms.ModelForm):
    description = forms.CharField(max_length=140,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a task...'}))

    class Meta:
        model = Task
