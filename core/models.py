from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=250)
    metric = models.PositiveIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    unit_of_measure = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records')
    finished_date = models.DateField(blank=True, null=True)
    amount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Record for {self.habit.name}"