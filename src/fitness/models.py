from django.db import models
from django.urls import reverse

class ExerciseType(models.TextChoices):
    ARMS = "A"
    BACK = "B"
    CHEST = "C"
    FULL_BODY = "F"
    LEGS = "L"
    SHOULDERS = "S"

class EquipmentType(models.TextChoices):
    BARBELL = "B"
    BODYWEIGHT = "BW"
    DUMBELL = "D"
    ROPES = "R"

class Exercise(models.Model):
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=1, choices=ExerciseType, default=ExerciseType.FULL_BODY)
    image = models.ImageField(upload_to="images/")
    equipment = models.CharField(max_length=2, choices=EquipmentType, default=EquipmentType.BODYWEIGHT)
    weight = models.JSONField(default=list)

    def __str__(self):
        return f"{self.name}. Type: {self.type}"
    
    def get_absolute_url(self):
        return reverse("exercise_detail", kwargs={"pk": self.pk})

class Workout(models.Model):
    name = models.CharField(max_length=100)
    focus = models.CharField(max_length=1, choices=ExerciseType, default=ExerciseType.FULL_BODY)
    exercises = models.ManyToManyField(
        Exercise,
        related_name="workout_exercises",
    )

    def __str__(self):
        return f"Name: {self.name}. Focus: {self.focus}"
    
class WorkoutObject(models.Model):
    pass