from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
    )
    
from .managers import AccountManager
from arealocations.models import AreaLocation

# Custom user created.
class Account(AbstractBaseUser, PermissionsMixin):
    username                = models.CharField(max_length=155, unique=True)
    email                   = models.EmailField(unique=True)
    area_location           = models.ForeignKey(AreaLocation, verbose_name=("Area Location"), on_delete=models.CASCADE, null=True, blank=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined             = models.DateTimeField(verbose_name='date join', auto_now_add=True)
    is_active               = models.BooleanField(default=True)
    is_rider                = models.BooleanField(default=False)
    is_hubmanager           = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        #Simplest possible answer: Yes, always
        return True

class RiderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_rider=True)

class Rider(Account):

    objects = RiderManager()
    
    class Meta:
        proxy = True

class TotalHubManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_hubmanager=True)

class HubManager(Account):

    objects = TotalHubManager()

    class Meta:
        proxy = True
