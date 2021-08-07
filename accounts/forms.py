from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import UserManager
from .models import Account, HubManager, Rider

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ['email', 'is_rider', 'is_hubmanager', 'is_staff']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'is_rider', 'is_hubmanager', 'is_staff']


class RiderRegisterForm(UserCreationForm):
    class Meta:
        model = Rider
        fields = ['username', 'email', 'area_location', 'password1', 'password2']

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            try:
                user = Account.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValueError(f'email {self.email} is Alredy used.')
        
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                user = Account.objects.get(username=username)
            except Exception as e:
                return username
            raise forms.ValueError(f'email {self.username} is Alredy used.')

class HubManagerRegisterForm(UserCreationForm):
    class Meta:
        model = HubManager
        fields = ['username', 'email', 'area_location', 'password1', 'password2']

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            try:
                user = Account.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValueError(f'email {self.user} is Alredy used.')
        
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                user = Account.objects.get(username=username)
            except Exception as e:
                return username
            raise forms.ValueError(f'email {self.user} is Alredy used.')


'''
class CustomHubManagerCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = HubManager
        fields = ['email', 'type',]

class CustomHubManagerChangeForm(UserChangeForm):
    class Meta:
        model = HubManager
        fields = ['email', 'username', 'type']

class CustomRiderCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Rider
        fields = ['email', 'type']

class CustomRiderChangeForm(UserChangeForm):
    class Meta:
        model = Rider
        fields = ['email', 'username', 'type']

'''