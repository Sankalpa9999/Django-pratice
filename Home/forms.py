
from django import forms 
from .models import Student 

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','city','image']

class UpdateStudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','city','image']