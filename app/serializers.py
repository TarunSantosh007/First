from rest_framework import serializers
from .models import movies



class moviesSerializers(serializers.ModelSerializer):

    class Meta:

        model = movies
        fields = "__all__"