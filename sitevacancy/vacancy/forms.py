from django import forms
from .models import Vacancy, Comment


class AddVacancy(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'company', 'text', 'salary', 'link']
        widgets = {
            'name': forms.TextInput(),
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


