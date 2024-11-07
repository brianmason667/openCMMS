# frontend/forms.py

from django import forms
from .models import Task, Equipment, Part

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'end_date', 'description', 'duration', 'equipment', 'teams', 'files']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'equipment_type', 'line', 'files']

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'line', 'description', 'end_date', 'duration', 'equipment']  # Include fields as needed

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'  # Or specify fields explicitly