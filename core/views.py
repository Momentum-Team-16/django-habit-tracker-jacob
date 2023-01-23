from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Record, Habit
from django.contrib.auth.decorators import login_required
from core.forms import HabitForm, RecordForm

# Create your views here.

@login_required
def index(request):
    habits = Habit.objects.all()
    return render(request, 'core/tracker.html', {'habits': habits})

def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')

def tracker_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'core/tracker.html', {'habit': habit})

def make_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES)
        if form.is_valid():
            habit = form.save()
            return redirect("main")
    else:
        form = HabitForm()
    return render(request, 'core/make_habit.html', {'form': form})

def edit_habit(request, habitpk):
    habit = get_object_or_404(Habit, pk=habitpk)
    if request.method == "POST":
        form = HabitForm(request.POST, request.FILES, instance=habit)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('tracker', pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'form': form})

def delete_habit(request, habitpk):
    habit = get_object_or_404(Habit, pk=habitpk)
    if request.method == 'POST':
        habit.delete()
        return redirect('main')
    return render(request, 'core/delete_habit.html')

def make_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            return redirect("main")
    else:
        form = RecordForm()
    return render(request, 'core/make_record.html', {'form': form})

