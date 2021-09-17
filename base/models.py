from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
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

    category = models.CharField(choices=CATEGORIES, max_length=4, verbose_name = "Kategoria")
    date = models.DateTimeField(auto_now_add=False,default=datetime.datetime.now())
    name = models.CharField(max_length=100, null=True, verbose_name = "Nazwa produktu")
    total_calories = models.IntegerField(verbose_name = "Kalorie")
    fat = models.IntegerField(verbose_name = "Tłuszcz")
    protein = models.IntegerField(verbose_name = "Proteiny")
    carbs = models.IntegerField(verbose_name = "Węglowodany")
    date_eaten = models.DateField(default=timezone.now,verbose_name = "Data spożycia")
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.category}/// {self.date_eaten}"

