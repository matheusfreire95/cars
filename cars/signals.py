from .models import Car, Inventory
from django.db.models import Sum
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver


def car_inventory_update():
    car_quantity = Car.objects.all().count()
    car_value = Car.objects.aggregate(
        car_total_value=Sum('value')
    )['car_total_value']
    
    Inventory.objects.create(
        car_quantity=car_quantity,
        car_value=car_value
    )


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

