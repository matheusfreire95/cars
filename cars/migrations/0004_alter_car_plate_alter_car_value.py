# Generated by Django 5.2 on 2025-05-30 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0003_car_photo_car_plate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="plate",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="value",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
