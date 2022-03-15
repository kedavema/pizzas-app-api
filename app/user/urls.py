from django.urls import path
from user.views import UsersAPIView, UserDetailAPIView

app_name = "user"


urlpatterns = [
    path("all", UsersAPIView.as_view(), name="get-users"),
    path("<int:pk>", UserDetailAPIView.as_view(), name="user-detail"),
]