from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    AllUserAccount,
    RiderRegisterView,
    HubManagerRegisterView,
    password_reset_request_view,
)

app_name = 'accounts'
urlpatterns = [
    path('all-users/', AllUserAccount.as_view(), name='all_users'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('rider-register/', RiderRegisterView.as_view(), name='rider_register'),
    path('hubmanager-register/', HubManagerRegisterView.as_view(), name='hubmanager_register'),
    path('password-reset/', password_reset_request_view, name='password_reset'),
]
