import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Jedzenie
from django import forms
import datetime
from django import forms
from datetime import timedelta


from django import forms

class EdutujDane(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")


class ExampleForm(forms.Form):
    OPTIONS = [
        (timedelta(minutes=5).total_seconds(), '5 mins'),
        (timedelta(minutes=10).total_seconds(), '10 mins'),
        (timedelta(minutes=30).total_seconds(), '30 mins'),
        (timedelta(hours=1).total_seconds(), '1 hour'),
        (timedelta(hours=3).total_seconds(), '3 hours'),
        (timedelta(hours=6).total_seconds(), '6 hours'),
        (timedelta(days=1).total_seconds(), '1 day'),
        (timedelta(days=2).total_seconds(), '2 day'),
        (timedelta(weeks=1).total_seconds(), '1 week'),
    ]

    time = forms.TypedChoiceField(choices=OPTIONS, coerce=lambda dt: timedelta(seconds=float(dt)))


class Homeform(forms.Form):
    text = forms.CharField(label='Your name', max_length=100)