from django import forms
from .models import Student, Course , Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('topic', 'languages_used', 'duration')
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'languages_used': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
}
