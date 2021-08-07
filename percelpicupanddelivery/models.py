from django.conf import settings
from django.db import models
from accounts.models import Rider
from percels.models import Percel
from django.utils.translation import ugettext_lazy as _

class PercelPicUp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pipup_rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='percelpicups')
    percel = models.ForeignKey(Percel, on_delete=models.CASCADE)
    is_active = models.BooleanField(_("Is Active"), default=True)
    completed = models.BooleanField(_("Completed"), default=False)

    def __str__(self):
        return f"{self.percel}/{self.user}"

class PercelPicupManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active=False)

class PercelPicupIncompleted(PercelPicUp):
    objects = PercelPicupManager()

    class Meta:
        proxy = True
    

class PercelDelivery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='parceldeliveries')
    picup_percel = models.ForeignKey(PercelPicupIncompleted, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.picup_percel}/{self.user}"
    
