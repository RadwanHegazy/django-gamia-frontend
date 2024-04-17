from django.urls import path
from .views import profile
from .views.auth import login, logout, register


urlpatterns = [
    path('auth/login/',login.LoginView.as_view(),name='login'),
    path('auth/register/',register.RegisterView.as_view(),name='register'),
    path('auth/logout/',logout.LogoutView.as_view(),name='logout'),
    path('',profile.ProfileView.as_view(),name='profile')
]