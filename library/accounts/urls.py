from django.urls import path
from .views import RegisterView, ProfileView

from .views import password_reset, password_reset_confirm


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

urlpatterns += [
    path(
        'password-reset/',
        password_reset,
        name='password_reset'
    ),
    path(
        'password-reset/confirm/',
        password_reset_confirm,
        name='password_reset_confirm'
    ),
]