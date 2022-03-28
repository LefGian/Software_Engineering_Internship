from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from userprofile.views import userprofile

urlpatterns = [
    path('', views.startsite, name="startsite-startseite"),
    path('logout/', auth_views.LogoutView.as_view(template_name='startsite/startseite.html'), name='logout'),
    path('profile/', userprofile, name="profile"),
]
