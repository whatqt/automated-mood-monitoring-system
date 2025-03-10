import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_mood_monitoring_system.settings')  # Замените на имя вашего проекта
django.setup()
from rest_framework import serializers
from data_processing.models import ResponsesAI

   

class ProcessingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsesAI
        fields = ["feedback", "data_for_analysis"]

