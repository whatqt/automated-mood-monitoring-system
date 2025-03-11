from django.db import models
from django.contrib.auth.models import User


class DataForAnalysis(models.Model):
    id = models.AutoField(primary_key=True)
    thema = models.CharField(max_length=75)
    msg = models.TextField()
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
    )
