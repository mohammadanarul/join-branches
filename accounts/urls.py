from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    AllUserAccount,
    password_reset_request_view,
)

app_name = 'accounts'
urlpatterns = [
    path('all-users/', AllUserAccount.as_view(), name='all_users'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('password-reset/', password_reset_request_view, name='password_reset'),
]
