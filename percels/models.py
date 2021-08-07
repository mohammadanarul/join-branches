from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from arealocations.models import AreaLocation
from picuplocations.models import PicupLocation

class CompletedPercelManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active=False)

class Percel(models.Model):
    user                        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    percel_unique_id            = models.CharField(max_length=50, unique=True, blank=True)
    picuplocation               = models.ForeignKey(PicupLocation, on_delete=models.CASCADE)
    customer_name               = models.CharField(max_length=255)
    customer_phone_number       = models.CharField(max_length=50)
    customer_address            = models.CharField(max_length=1000)
    product_weight              = models.PositiveIntegerField(default=1)
    area_location               = TreeForeignKey(AreaLocation, on_delete=models.CASCADE)
    product_price               = models.PositiveIntegerField(default=1)
    customerdetails             = models.TextField()
    is_active                   = models.BooleanField(default=True)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    NewObjects = CompletedPercelManager()

    def __str__(self):
        return f'{self.customer_name}-{self.pk}'

    ordering_by = '-created_at'

class PercelManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active=True)

class IncompletePercelPicupManager(Percel):

    objects = PercelManager()

    class Meta:
        proxy = True
    






