from django import forms
from .models import Workout, Exercise

class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["name", "focus", "exercises"]

