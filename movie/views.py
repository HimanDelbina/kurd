from asyncio.windows_events import NULL
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
def get_all_movie(request):
    store_data = MovieModel.objects.all()
    return Response(
        MovieSerializers(store_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def get_moviee_by_genre_id(request, id):
    data = MovieModel.objects.filter(genre_id=id)
    return Response(MovieSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_moviee_by_director_id(request, id):
    data = MovieModel.objects.filter(director_id=id)
    return Response(MovieSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_moviee_by_category_id(request, id):
    data = MovieModel.objects.filter(director_id=id)
    return Response(MovieSerializers(data, many=True).data, status=status.HTTP_200_OK)
