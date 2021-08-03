from django.shortcuts import render
from rest_framework import viewsets
from .models import Video
from .serializer import VideoSerializer

# Create your views here.

class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
