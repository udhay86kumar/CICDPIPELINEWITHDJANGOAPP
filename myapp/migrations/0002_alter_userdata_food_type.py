# Generated by Django 5.1.1 on 2024-10-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdata",
            name="food_type",
            field=models.CharField(
                choices=[("Veg", "Veg"), ("Non-Veg", "Non-Veg")], max_length=100
            ),
        ),
    ]
