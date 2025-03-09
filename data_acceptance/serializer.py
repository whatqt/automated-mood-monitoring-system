from rest_framework import serializers
from .models import DataForAnalysis


class DataAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataForAnalysis
        fields = "__all__"