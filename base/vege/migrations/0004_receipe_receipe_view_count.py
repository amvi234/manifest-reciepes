# Generated by Django 4.2.7 on 2023-12-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0003_receipe_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipe",
            name="receipe_view_count",
            field=models.IntegerField(default=1),
        ),
    ]
