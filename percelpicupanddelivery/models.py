from django.conf import settings
from django.db import models
from accounts.models import Rider

PICUP_AND_DELIVERY_STATUS = (
    ('PICUP', 'Picup'),
    ('DELIVERY', 'Delivery'),
    ('PROCESSING', 'Processing'),
    ('COMPLETE', 'Complete'),
)

class PercelPicUpAndDelivery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pipuprider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='percelpicups')
    # percel = models.ForeignKey(PercelProssesing, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=PICUP_AND_DELIVERY_STATUS)
