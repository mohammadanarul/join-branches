from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
    )
    
from .managers import AccountManager

# Custom user created.
class Account(AbstractBaseUser, PermissionsMixin):
    class UserTypes(models.TextChoices):
        RIDER                   = 'PRIDER', 'Rider'
        HUBMANAGER              = 'HUBMANAGER', 'Hubmanager'
    
    base_type = UserTypes.RIDER

    type                    = models.CharField(choices=UserTypes.choices, default=base_type, max_length=20)
    username                = models.CharField(max_length=155, unique=True)
    email                   = models.EmailField(unique=True)
    # area                    = models.ForeignKey(AreaLocation, verbose_name=("Area Location"), on_delete=models.CASCADE)
    area_location           = models.CharField(max_length=1000) 
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined             = models.DateTimeField(verbose_name='date join', auto_now_add=True)
    is_active               = models.BooleanField(default=True)
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
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

class RiderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.UserTypes.RIDER)

class Rider(Account):
    base_type = Account.UserTypes.RIDER
    objects = RiderManager()
    
    class Meta:
        proxy = True

class TotalHubManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type = Account.UserTypes.HUBMANAGER)

class HubManager(Account):
    base_type = Account.UserTypes.HUBMANAGER
    objects = TotalHubManager()

    class Meta:
        proxy = True
