from django.db import models

class DataForAnalysis(models.Model):
    id = models.AutoField(primary_key=True)
    thema = models.CharField(max_length=75)
    msg = models.TextField()
