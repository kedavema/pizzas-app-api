from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from product.utils import resource_checker


class UsersAPIView(APIView):

    def get(self, request, format=None):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
      
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    @resource_checker(get_user_model())
    def get(self, request, pk, format=None):
        user = get_user_model().objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @resource_checker(get_user_model())
    def put(self, request, pk, format=None):
        user = get_user_model().objects.filter(id=pk).first()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    @resource_checker(get_user_model())
    def delete(self, request, pk, format=None):
        user = get_user_model().objects.filter(id=pk).first()
        user.delete()
        return Response({"message": f"User '{user}' deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
