from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise, Workout
from .forms import *

# WORKOUTS
def workouts(request):
    workouts = Workout.objects.all()
    context = {
        "workouts": workouts,
    }
    return render(request, "fitness/workouts.html", context=context)

def start_workout(request):
    # Render Workout Form
    workouts = Workout.objects.all()
    context = {
        "workouts": workouts
    }
    return render(request, "fitness/start_workout.html", context=context)

def workout_detail(request, name):
    workout = get_object_or_404(Workout, name=name)
    context = {
        "workout": workout,
    }
    return render(request, "fitness/workout_detail.html", context=context)

def create_new_workout(request):
    if request.method == 'POST':
        form = CreateWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts')
    else:
        form = CreateWorkoutForm()

    return render(request, "fitness/create_new_workout.html", {"form": form})

def delete_workout(request, id):
    obj = get_object_or_404(Workout, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('workouts')
    return render(request, "fitness/delete_confirmation.html", {})

# EXERCISES:
def exercises(request):
    exercise_list = Exercise.objects.all()
    context = {
        "exercise_list": exercise_list 
    }
    return render(request, "fitness/exercises.html", context=context)

def exercise_detail(request, name):
    exercise = Exercise.objects.get(name=name)
    context = {
        "exercise": exercise,
    }
    return render(request, "fitness/exercise_detail.html", context=context)
