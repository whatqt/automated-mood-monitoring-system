from django.db import models
from data_acceptance.models import DataForAnalysis


class ResponsesAI(models.Model):
    data_for_analysis = models.ForeignKey(
        DataForAnalysis,
        on_delete=models.CASCADE
    )
    feedback = models.TextField()

