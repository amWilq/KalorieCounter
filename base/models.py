from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import timedelta
import datetime


class Jedzenie(models.Model):

    Sniadanie = 'S'
    Sniadanie_II = 'S_II'
    Lunch = 'L'
    Obiad = 'O'
    Przekąska = 'P'
    Kolacja = 'K'
    Trening = 'T'
    Woda = 'W '

    CATEGORIES = [
        (Sniadanie, 'Sniadanie'),
        (Sniadanie_II, 'Sniadanie_II'),
        (Lunch, 'Lunch'),
        (Obiad, 'Obiad'),
        (Przekąska, 'Przekąska'),
        (Kolacja, 'Kolacja'),
        (Trening, 'Trening'),
        (Woda, 'Woda'),
    ]

    category = models.CharField(choices=CATEGORIES, max_length=4, default="Sniadanie")
    date = models.DateTimeField(auto_now_add=False,default=datetime.datetime.now())
    name = models.CharField(max_length=100, null=True)
    total_calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    date_eaten = models.DateField(auto_now_add=False, default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=User)

    def __str__(self):
        return f"{self.category}/// {self.date_eaten}"


