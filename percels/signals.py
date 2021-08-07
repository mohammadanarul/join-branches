from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Percel
from .unique_percel_generator import unique_random_string_generator



@receiver(post_save, sender=Percel)
def create_percel(sender, instance, created, **kwargs):
    if not instance.percel_unique_id:
        instance.percel_unique_id = unique_random_string_generator(size=20)
        instance.save()