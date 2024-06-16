from rest_framework import serializers
from .models import *


class MusicVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = MusicVideoModel
        fields = "__all__"
        depth = 1


class MusicMp3Serializers(serializers.ModelSerializer):
    class Meta:
        model = MusicMp3Model
        fields = "__all__"
        depth = 1


class SignerSerializers(serializers.ModelSerializer):
    class Meta:
        model = SingerModel
        fields = "__all__"


class CategoryMusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryMusicModel
        fields = "__all__"
