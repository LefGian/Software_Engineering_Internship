from django.contrib import admin
from .models import Aufgabe, Fachgebiet, Themengebiet

# Register your models here. So that they are shown in the admin page

admin.site.register(Aufgabe)
admin.site.register(Fachgebiet)
admin.site.register(Themengebiet)
