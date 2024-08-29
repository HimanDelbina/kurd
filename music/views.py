
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_music_video(request):
    store_data = MusicVideoModel.objects.all()
    return Response(
        MusicVideoSerializers(store_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_music_mp3(request):
    store_data = MusicMp3Model.objects.all()
    return Response(
        MusicMp3Serializers(store_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_music_mp3_by_category_id(request, id):
    data = MusicMp3Model.objects.filter(category_id=id)
    return Response(
        MusicMp3Serializers(data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_music_video_by_category_id(request, id):
    data = MusicVideoModel.objects.filter(category_id=id)
    return Response(
        MusicVideoSerializers(data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_music_video_by_signer_id(request, id):
    data = MusicVideoModel.objects.filter(signer_id=id)
    return Response(
        MusicVideoSerializers(data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_music_mp3_by_signer_id(request, id):
    data = MusicMp3Model.objects.filter(signer_id=id)
    return Response(
        MusicMp3Serializers(data, many=True).data, status=status.HTTP_200_OK
    )
