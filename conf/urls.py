from atexit import register
from django.contrib import admin
from django.urls import path, include
from notes import views as notes_view
from django.contrib.auth import views as auth
from notes.views import delete_note, note_update

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('notes.urls')),
    path('login/', notes_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', notes_view.register, name='register'),
    path('create_note/', notes_view.create_note, name='create_note'),
    path('delete/<str:drug_id>/', delete_note),
    path('edit/<int:id>/change/', note_update,name='edit')
]
