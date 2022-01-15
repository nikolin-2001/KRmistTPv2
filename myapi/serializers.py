from rest_framework import serializers

from .models import Operativka, Videocard

class OperativkaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operativka
        fields = ('name', 'image', 'price', 'pamyat', 'description')

class VideocardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videocard
        fields = ('name', 'image', 'price', 'pamyat', 'mochnost', 'description')
