from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializer import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

