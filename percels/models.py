from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from accounts.models import (
    Rider,
)

class AreaLocation(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by=['name']
    
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k= k.parent
        return '/'.join(full_path[::-1])

# Create your models here.
class PicupLocation(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picupname           = models.CharField(max_length=255)
    picupaddress        = models.CharField(max_length=1000)
    picup_area           = models.ForeignKey(AreaLocation, on_delete=models.CASCADE)
    shop_phone_number   = models.CharField(max_length=1000)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.picupname

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

    # objects = PercelManager()
    # NewObjects = PercelManager()

    def __str__(self):
        return f'{self.customer_name}-{self.pk}'

    ordering_by = '-created_at'

class PercelManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active=False)

class PercelComplete(Percel):

    objects = PercelManager()

    class Meta:
        proxy = True


class PercelProssesingManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active=True)

class PercelProssesing(Percel):

    objects = PercelProssesingManager()

    class Meta:
        proxy = True

PICUP_AND_DELIVERY_STATUS = (
    ('PICUP', 'Picup'),
    ('DELIVERY', 'Delivery'),
    ('PROCESSING', 'Processing'),
    ('COMPLETE', 'Complete'),
)

class PercelPicUpAndDelivery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pipuprider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='percelpicups')
    percel = models.ForeignKey(PercelProssesing, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=PICUP_AND_DELIVERY_STATUS)
    






