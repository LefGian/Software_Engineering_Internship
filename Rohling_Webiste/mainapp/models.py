from django.db import models


class Aufgabe(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField()
    thema = models.TextField(max_length=50)
    bearbeitungszeit = models.IntegerField()
    schwierigkeitsgrad  = models.IntegerField()


    def __str__(self):
        """specify how to default cast Aufgabe"""
        return self.title