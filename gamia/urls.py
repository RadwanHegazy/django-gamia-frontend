from django.urls import path
from .views import get,create

urlpatterns = [
    path('get/<str:gamia_id>/',get.GetGamiaView.as_view(),name='get_gamia'),
    path('create/',create.CreateGamiaView.as_view(),name='create_gamia'),
]