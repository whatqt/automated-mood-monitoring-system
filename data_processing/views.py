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

    def get_queryset_all(self, username_id):
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
                "id": response_ai.id,
                "thema": data_for_analysis.thema,
                "msg": data_for_analysis.msg,
                "feedback": response_ai.feedback
            }
            serializer = GetResponsesAiSerializer(data)
            all_data.append(serializer.data)

        return all_data
    
    def get_queryset_id(self, username_id, id_response):
        try:
            data_for_analysis = DataForAnalysis.objects.filter(
                username=username_id,
                id=id_response
            ).get()
        except ObjectDoesNotExist:
            return None
        response_ai = ResponsesAI.objects.filter(
            data_for_analysis=data_for_analysis.id
        ).get()
        print(response_ai.id)
        data = {
            "id": response_ai.id,
            "thema": data_for_analysis.thema,
            "msg": data_for_analysis.msg,
            "feedback": response_ai.feedback
        }
        serializer = GetResponsesAiSerializer(data=data)
        if serializer.is_valid():
            return serializer.data
        return serializer.errors

    def get(self, request: Request, id_response=0):
        if id_response == 0:
            data = self.get_queryset_all(request.user.pk)
            return Response(data, status=status.HTTP_302_FOUND)
        else:
            data = self.get_queryset_id(request.user.pk, id_response)
            if data:
                return Response(data, status=status.HTTP_302_FOUND)
            return Response(
                {"obj": None},
                status=status.HTTP_404_NOT_FOUND
            )