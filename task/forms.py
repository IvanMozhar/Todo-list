from django import forms
from django.contrib.auth import get_user_model

from task.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
        ]
        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "deadline": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
