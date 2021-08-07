from django.db import models
from django.conf import settings
from arealocations.models import AreaLocation

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
        return f"{self.picupname}-({self.user})"
