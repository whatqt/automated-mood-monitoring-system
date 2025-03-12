from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializer import GetResponsesAiSerializer
from rest_framework.permissions import IsAuthenticated
from .models import ResponsesAI
from data_acceptance.models import DataForAnalysis
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class GetResponsesAi(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, username_id):
        id_for_analysis = DataForAnalysis.objects.filter(
            username=username_id
        ).values_list("id", flat=True)
        all_data = []
        for id_data in id_for_analysis:
            try:
                response_ai = ResponsesAI.objects.get(data_for_analysis=id_data)
            except ObjectDoesNotExist:
                return all_data
            data_for_analysis = DataForAnalysis.objects.filter(id=id_data).get()
            data = {
                "thema": data_for_analysis.thema,
                "msg": data_for_analysis.msg,
                "feedback": response_ai.feedback
            }
            serializer = GetResponsesAiSerializer(data)
            all_data.append(serializer.data)

        return all_data
    
    def get(self, request: Request):
        data = self.get_queryset(request.user.pk)
        return Response(data, status=status.HTTP_302_FOUND)