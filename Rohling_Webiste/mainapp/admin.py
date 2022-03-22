from django.contrib import admin

# import Models to show:
from .models import Aufgabe


# register models in Adminseite:
admin.site.register(Aufgabe)
