from django.urls import path
from .views import register, editprofile

urlpatterns = [
    path('register/',register.as_view(),name='register'),
    path('edit_profile/',editprofile.as_view(),name='edit_profile'),
]