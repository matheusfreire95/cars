from .models import Car, Inventory
from openai_api.client import get_car_ai_bio
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


def car_bio_update(instance):
    if not instance.bio:
        try:
            ai_bio = get_car_ai_bio(
                instance.model, instance.brand, instance.model_year
            )

            instance.bio = ai_bio.content
            
        except Exception as e:
            instance.bio = "Descrição não disponível no momento."


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_bio_update(instance)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

