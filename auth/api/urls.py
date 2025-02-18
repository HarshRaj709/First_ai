from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenBlacklistView


urlpatterns = [
    path('registration/',views.UserRegistrationView.as_view(),name='registeration'),
    path('login/',views.LoginUser.as_view(),name='api_login'),
    # path('logout/',views.LogoutUser.as_view(),name='logout'),
    path('logout/',TokenBlacklistView.as_view(),name='api_logout'),
    path('password_reset/',views.Password_Reset.as_view(),name='Password_Reset'),
    path('reset/<str:uidb64>/<str:token>/', views.ResetPasswordAPIView.as_view(), name='password_reset_confirm'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('google-login/', views.GoogleLoginView.as_view(), name='google_login'),
]
