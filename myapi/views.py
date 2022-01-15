from rest_framework import viewsets

from .serializers import OperativkaSerializer, VideocardSerializer
from .models import Operativka, Videocard

class OperativkaViewSet(viewsets.ModelViewSet):
    queryset = Operativka.objects.all().order_by('name')
    serializer_class = OperativkaSerializer

class VideocardViewSet(viewsets.ModelViewSet):
    queryset = Videocard.objects.all().order_by('name')
    serializer_class = VideocardSerializer
