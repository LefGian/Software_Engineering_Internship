from django.contrib import admin
from .models import Aufgabe, Fachgebiet,Themengebiet

# Register your models here.

admin.site.register(Aufgabe)
admin.site.register(Fachgebiet)
admin.site.register(Themengebiet)