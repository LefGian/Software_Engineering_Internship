from django.urls import path
from . import views

urlpatterns = [
    path('', views.createassignment, name="createassignment-createassignment"),
]
