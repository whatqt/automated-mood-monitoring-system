from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializer import DataAcceptanceSerializer
from rest_framework import status
from .producer import SendData
from json import dumps
from rest_framework.permissions import IsAuthenticated
from automated_mood_monitoring_system.decoratos import insert_user_pk
from .models import DataForAnalysis

class DataAcceptance(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self, username_id):
        data = DataForAnalysis.objects.filter(
            username=username_id
        ).values()
        return data

    @insert_user_pk
    def post(self, request: Request):
        serializer = DataAcceptanceSerializer(
            data=request.data
        )
        print(type(request.data))
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

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def get(self, request: Request, id=0):
        data = self.get_queryset(request.user.pk)
        print(data)
        all_data = []
        for info in data:
            serializer = DataAcceptanceSerializer(
                data=info
            )
            if serializer.is_valid():
                all_data.append(info)
            else: 
                return Response(
                    serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {"data": all_data}, 
            status=status.HTTP_302_FOUND
        )
        
# {"thema":"test", "msg":"test"}