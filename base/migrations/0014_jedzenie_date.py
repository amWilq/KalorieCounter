# Generated by Django 3.2.4 on 2021-08-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_jedzenie_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='jedzenie',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
