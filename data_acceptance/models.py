from django.db import models

class DataForAnalysis(models.Model):
    thema = models.CharField(max_length=75)
    msg = models.TextField()
