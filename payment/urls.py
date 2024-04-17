from django.urls import path
from .views import success, cancel


urlpatterns = [
    path('success/<str:payment_id>/<str:user_token>/',success.SuccessView.as_view(),name='success'),
    path('cancel/<str:payment_id>/<str:user_token>/',cancel.CancelView.as_view(),name='cancel'),
]