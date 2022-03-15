from unicodedata import name
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import UsersAPIView, UserDetailAPIView

app_name = "user"


urlpatterns = [
    path("all", UsersAPIView.as_view(), name="users"),
    path("<int:pk>", UserDetailAPIView.as_view(), name="user-detail"),
    path('api-token-auth', views.obtain_auth_token, name='token'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
