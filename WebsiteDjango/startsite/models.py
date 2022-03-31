from django.db import models
from django.contrib.auth.models import User


class Fachgebiet(models.Model):
    name = models.TextField()

    def __str__(self):
        """specify how to default cast Fachgebiet"""
        return str(self.name)


class Themengebiet(models.Model):
    name = models.TextField()
    fachgebiet = models.ForeignKey(Fachgebiet, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """specify how to default cast Themenegebiet"""
        return str(self.name)


class Aufgabe(models.Model):
    name = models.TextField()
    aufgabenstellung = models.TextField()
    loesung = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    schwierigkeit = models.PositiveIntegerField()
    zeit = models.PositiveIntegerField()
    themengebiet = models.ForeignKey(Themengebiet, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """specify how to default cast Aufgabe"""
        return str(self.name)
