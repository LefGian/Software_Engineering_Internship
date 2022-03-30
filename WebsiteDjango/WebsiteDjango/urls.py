from django.contrib import admin
from django.urls import path, include

import createassignment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('startsite/', include('startsite.urls')),
    path('', include('startsite.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('home/', include('home.urls')),
    path('createassignment/', include('createassignment.urls')),
]
