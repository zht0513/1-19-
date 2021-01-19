from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from api
from api.authentication import MyAuthentication
from api.serializer import UserModelSerializer


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [MyAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({"username": request.user.username})


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "user": UserModelSerializer(serializer.obj).data,
            "token": serializer.token
        })
