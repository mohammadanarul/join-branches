from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, ReadOnlyPasswordHashWidget
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from .models import (
    Account,
    HubManager,
    Rider,
)


@admin.register(Account)
class UserAccountModelAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('username', 'date_joined')
    readonly_fields = ('pk', 'date_joined', 'last_login')
    filter_horizontal = []
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'type', 'password1', 'password2')}
        ),
    )

@admin.register(Rider)
class RiderAdminModel(admin.ModelAdmin):
    # add_form = CustomRiderCreateForm
    # form = CustomRiderChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'type', 'password1', 'password2')}
        ),
    )
    readonly_fields = ('pk', 'date_joined', 'last_login')

@admin.register(HubManager)
class HubManagerAdminModel(admin.ModelAdmin):
    # add_form = CustomHubManagerCreateForm
    # form = CustomHubManagerChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'type')}
        ),
    )
    readonly_fields = ('pk', 'date_joined', 'last_login')


