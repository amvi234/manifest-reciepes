# Generated by Django 4.0.6 on 2024-06-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0008_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='receipe_image',
        ),
        migrations.AddField(
            model_name='receipe',
            name='receipe_price',
            field=models.IntegerField(default=0),
        ),
    ]
