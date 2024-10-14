from rest_framework import serializers
from .models import *


class PodcastGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = PodcastModel
        fields = "__all__"
        depth = 1


class PodcastSerializers(serializers.ModelSerializer):
    class Meta:
        model = PodcastModel
        fields = "__all__"


class PodcastVideoGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = PodcastVideoModel
        fields = "__all__"
        depth = 1


class PodcastVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PodcastVideoModel
        fields = "__all__"
