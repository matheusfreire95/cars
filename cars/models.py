from django.db import models


class Inventory(models.Model):
    car_quantity = models.IntegerField()
    car_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.car_quantity} cars - ${self.car_value:.2f}' if self.car_value is not None else f'{self.car_quantity} cars'


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)

    def __str__(self):
        return self.model
