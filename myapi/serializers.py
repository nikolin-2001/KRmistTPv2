from rest_framework import serializers

from .models import Operativka, Videocard, Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner']

class OperativkaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operativka
        fields = ('name', 'price', 'pamyat', 'description')

class VideocardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videocard
        fields = ('name', 'price', 'pamyat', 'mochnost', 'description')
