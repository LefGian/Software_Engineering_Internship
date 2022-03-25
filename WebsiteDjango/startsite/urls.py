from django.urls import path
from . import views

urlpatterns = [
    path('', views.startsite, name="startsite-startseite"),
]
