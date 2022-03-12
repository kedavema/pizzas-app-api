from django.urls import path
from user.views import user_api_view, user_detail_api_view

app_name = "user"


urlpatterns = [
    path("users/", user_api_view, name="get-users"),
    path("users/<int:pk>", user_detail_api_view, name="user-detail"),
]