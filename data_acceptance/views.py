from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializer import DataAcceptanceSerializer
from rest_framework import status
from .producer import SendData
from json import dumps
from rest_framework.permissions import IsAuthenticated
from automated_mood_monitoring_system.decoratos import insert_user_pk


class DataAcceptance(APIView):
    permission_classes = [IsAuthenticated]
    
    @insert_user_pk
    def post(self, request: Request):
        serializer = DataAcceptanceSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            data = {
                "data_for_analysis": serializer.data["id"],
                "thema": serializer.data["thema"],
                "msg": serializer.data["msg"]
            }
            send_data = SendData(dumps(data))
            send_data.send()       
            return Response(
                {"status": "the data is saved and sended"},
                status=status.HTTP_202_ACCEPTED
            )

        return Response(serializer.errors)


# {"thema":"test", "msg":"test"}