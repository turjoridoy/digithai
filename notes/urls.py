from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import notes
from notes.views import NoteViewSet

router = routers.SimpleRouter()
router.register(r'note', NoteViewSet)

urlpatterns = [
    # path('note/', create_note),
    path('', notes.views.index, name='index'),
]

urlpatterns += router.urls