from rest_framework import serializers
from .models import *


class ToturialSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToturialModel
        fields = "__all__"
