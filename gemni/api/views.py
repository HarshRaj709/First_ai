from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from gemni.ai_client import GoogleAIClient
from .serializers import FormSerializer, UserHistorySerializer
from rest_framework import status
from ai.settings import api_key
from gemni.services import generate_travel_suggestions,format_response
from gemni.models import UserHistory


class form(CreateAPIView):
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticated]

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            form_data = serializer.validated_data

            ai_client = GoogleAIClient(api_key = api_key)
            response_text = generate_travel_suggestions(form_data,ai_client)
            formatted_text = format_response(response_text)

            return Response({'form_data':form_data,"travel_suggestion":formatted_text},
                            status = status.HTTP_201_CREATED)
        else:
            return Response({'Error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class UserSearch(ListAPIView):
    serializer_class = UserHistorySerializer
    permission_classes = [IsAuthenticated]
    queryset = UserHistory.objects.all()