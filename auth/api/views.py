
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserRegistration, LoginSerializers,Password_ResetSerializer,Password_changedSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings




def get_tokens(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistration
    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                token = get_tokens(user)
                return Response({"msg": "User created successfull", "token": token}, status=status.HTTP_201_CREATED)
            return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_OAUTH2_CLIENT_ID)
            # print(idinfo)

            userid = idinfo['sub']
            email = idinfo['email']
            name = idinfo.get('name', '')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User.objects.create_user(username=email, email=email, first_name=name)
            tokens = get_tokens(user)

            return Response({
                'msg': 'Login Successful',
                'tokens': tokens,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'name': user.first_name,
                }
            }, status=status.HTTP_200_OK)

        except ValueError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)





class LoginUser(CreateAPIView):
    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg": "Login Successful", "token": get_tokens(user)}, status=status.HTTP_200_OK)
    


class Password_Reset(APIView):
    @swagger_auto_schema(request_body=Password_ResetSerializer)
    def post(self, request, format=None):
        serializer = Password_ResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email = email)
            if not user:
                return Response({'error': 'User with this email does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = f"Testing/auths/reset/{uidb64}/{token}/"
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link below to reset your password:\n{reset_link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            return Response({'msg': 'Email sent to recover the password'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ResetPasswordAPIView(APIView):
    @swagger_auto_schema(request_body=Password_changedSerializer)
    def post(self, request, uidb64, token):  
        refresh = request.data.get('refresh')
        serializer = Password_changedSerializer(data=request.data,context={'uidb64': uidb64, 'token': token,'refresh':refresh}) 
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Password changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Generic Logout
# class LogoutUser(GenericAPIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request,format=None):
#         refresh = request.data.get('refresh')
#         # print(refresh)
#         if not refresh:
#             return Response({"msg":"refresh token is required"},status=status.HTTP_400_BAD_REQUEST)
#         else:
#             try:
#                 token = RefreshToken(refresh)
#                 token.blacklist()
#                 return Response({"msg":"Logged out successfully"},status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response({"msg":f"Error: {e}"},status=status.HTTP_400_BAD_REQUEST)