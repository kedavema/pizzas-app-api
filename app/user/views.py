from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from product.utils import resource_checker
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer


class UsersAPIView(APIView):
    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    def get(self, request, format=None):
        """Return a list of User objects"""
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(responses={201: UserSerializer()})
    def post(self, request, format=None):
        """Create a new User object"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    @swagger_auto_schema(responses={200: UserSerializer()})
    @resource_checker(get_user_model())
    def get(self, request, pk, format=None):
        """Get an User object by ID"""
        user = get_user_model().objects.get(pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserSerializer()})
    @resource_checker(get_user_model())
    def put(self, request, pk, format=None):
        """Update an user object"""
        user = get_user_model().objects.filter(id=pk).first()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: "User deleted succesfully"})
    @resource_checker(get_user_model())
    def delete(self, request, pk, format=None):
        """Delete an User object"""
        user = get_user_model().objects.filter(id=pk).first()
        user.delete()

        return Response(
            {"message": f"User '{user}' deleted succesfully"},
            status=status.HTTP_204_NO_CONTENT
        )
