from rest_framework import viewsets, generics

from . import serializers
from .serializers import OperativkaSerializer, VideocardSerializer, PostSerializer
from .models import Operativka, Videocard, Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class OperativkaViewSet(viewsets.ModelViewSet):
    queryset = Operativka.objects.all().order_by('name')
    serializer_class = OperativkaSerializer

class VideocardViewSet(viewsets.ModelViewSet):
    queryset = Videocard.objects.all().order_by('name')
    serializer_class = VideocardSerializer
