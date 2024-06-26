from django import forms
from .models import Task, SubTask

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea)


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "completed_at",
            "status"
        ]


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = [
            "title",
            "description",
            "related_task"
        ]


class SubTaskUpdateForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = [
            "title",
            "description",
            "status"
        ]
