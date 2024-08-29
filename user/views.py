from ast import Store
from urllib import response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.decorators import permission_classes, api_view
from django.core.files.base import ContentFile
import base64
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    s_data = request.data
    users = UserSerializers(data=s_data)
    data = {}
    user_check = UserModel.objects.filter(email=request.data["email"]).first()
    if user_check is not None:
        return Response("user is allow...", status=status.HTTP_208_ALREADY_REPORTED)
    else:
        if users.is_valid():
            account = users.save()
            data["first_name"] = account.first_name
            data["last_name"] = account.last_name
            data["email"] = account.email
            data["password"] = account.password
            data["create_at"] = account.create_at
            data["update_at"] = account.update_at
            token = MyOwnToken.objects.get(userTokens=account).key
            data["token"] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response("user not create...", status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    info = {}
    user = UserModel.objects.filter(
        email=request.data["email"], password=request.data["password"]
    ).first()
    if user is not None:
        token = MyOwnToken.objects.get(userTokens=user).key
        info["id"] = user.id
        info["first_name"] = user.first_name
        info["last_name"] = user.last_name
        info["email"] = user.email
        info["token"] = token
        return Response(info, status=status.HTTP_200_OK)
    else:
        return Response(
            "The entered data is incorrect", status=status.HTTP_204_NO_CONTENT
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def delete_user_by_id(request, id):
    user_data_for_delete = UserModel.objects.filter(id=id)
    user_data_for_delete.delete()
    return Response("user is delete...", status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def edit_user(request):
    etid_data = request.data
    edit_data_find_in_database = UserModel.objects.get(id=etid_data["id"])
    edit_data_find_in_database.first_name = etid_data["first_name"]
    edit_data_find_in_database.last_name = etid_data["last_name"]
    edit_data_find_in_database.email = etid_data["email"]
    edit_data_find_in_database.password = etid_data["password"]
    edit_data_find_in_database.save()
    return Response("user is update succesfully....", status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_user(request):
    user_data = UserModel.objects.all()
    return Response(
        UserSerializers(user_data, many=True).data, status=status.HTTP_200_OK
    )
