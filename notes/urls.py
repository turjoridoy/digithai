from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from notes.views import NoteViewSet

router = routers.SimpleRouter()
router.register(r'note', NoteViewSet)

urlpatterns = [
    # path('note/', create_note),
]

urlpatterns += router.urls