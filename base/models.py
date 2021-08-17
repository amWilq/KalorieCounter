from django.db import models
from django.contrib.auth.models import User



class Jedzenie(models.Model):
    CATEGORIES = (
        ('S', 'Sniadanie'),
        ('S_II', 'Sniadanie II'),
        ('L', 'Lunch'),
        ('O', 'Obiad'),
        ('C', 'Przekąska'),
        ('K', 'Kolacja'),
        ('T', 'Trening'),
        ('W', 'Woda')
    )
    category = models.CharField(choices=CATEGORIES, max_length=4, default="Sniadanie")

    name = models.CharField(max_length=100, null=True)
    total_calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    #category = models.CharField(choices=CATEGORIES,max_length=4)
    date_eaten = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.category}/// {self.date_eaten}"


class Calorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    calorie = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            'calorie'
        ]

