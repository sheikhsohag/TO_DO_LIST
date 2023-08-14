from django import forms
from works.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription']