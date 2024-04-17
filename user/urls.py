from django.urls import path, include
from .views import profile
from .views.pay import charge, withdraw
from .views.auth import login, logout, register


urlpatterns = [
    path('auth/login/',login.LoginView.as_view(),name='login'),
    path('auth/register/',register.RegisterView.as_view(),name='register'),
    path('auth/logout/',logout.LogoutView.as_view(),name='logout'),
    path('',profile.ProfileView.as_view(),name='profile'),
    path('charge/',charge.ChargeView.as_view(),name='charge'),
    path('withdraw/',withdraw.WithdrawView.as_view(),name='withdraw'),
]