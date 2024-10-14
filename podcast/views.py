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
def get_all_podcast_video(request):
    store_data = PodcastVideoModel.objects.all()
    return Response(
        PodcastVideoGetSerializers(store_data, many=True).data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_podcast_mp3(request):
    store_data = PodcastModel.objects.all()
    return Response(
        PodcastGetSerializers(store_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_podcast_mp3_by_category_id(request, id):
    data = PodcastModel.objects.filter(category_id=id)
    return Response(
        PodcastGetSerializers(data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_podcast_video_by_category_id(request, id):
    data = PodcastVideoModel.objects.filter(category_id=id)
    return Response(
        PodcastVideoGetSerializers(data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_podcast_mp3_by_signer_id(request, id):
    data = PodcastModel.objects.filter(signer_id=id)
    return Response(
        PodcastGetSerializers(data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_podcast_video_by_signer_id(request, id):
    data = PodcastVideoModel.objects.filter(signer_id=id)
    return Response(
        PodcastVideoGetSerializers(data, many=True).data, status=status.HTTP_200_OK
    )
