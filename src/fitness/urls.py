from django.urls import path
from . import views
from .models import Exercise

urlpatterns = [
    path("workouts/", views.workouts, name="workouts"),
    path("workouts/start", views.start_workout, name="start_workout"),
    path("workouts/<str:name>", views.workout_detail, name="workout_detail"),
    path("workouts/create_new_workout/", views.create_new_workout, name="create_new_workout"),
    path("workouts/delete_workout/<int:id>", views.delete_workout, name="delete_workout"),

    path("exercises/", views.exercises, name="exercises"),
    path("exercises/<str:name>", views.exercise_detail, name="exercise_detail")
]