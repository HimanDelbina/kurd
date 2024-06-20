from rest_framework import serializers
from .models import *


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = "__all__"


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class ProducerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProducerModel
        fields = "__all__"


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyShowModel
        fields = "__all__"
        depth = 1
