from django.db import models
from django.contrib.auth.models import User


class Aufgabe(models.Model):
    name = models.TextField()
    aufgabenstellung = models.TextField()
    loesung = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    schwierigkeit = models.PositiveIntegerField()
    zeit = models.PositiveIntegerField()
    themengebiet = models.TextField()
    fachgebiet = models.TextField()

    def __str__(self):
        """specify how to default cast Aufgabe"""
        return str(self.name)
