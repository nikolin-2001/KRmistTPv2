from rest_framework import serializers

from .models import Operativka, Videocard, Tutorial

class OperativkaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operativka
        fields = ('name', 'price', 'pamyat', 'description')

class VideocardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videocard
        fields = ('name', 'price', 'pamyat', 'mochnost', 'description')


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')