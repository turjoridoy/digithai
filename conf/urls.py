from atexit import register
from django.contrib import admin
from django.urls import path, include
from notes import views as notes_view
from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('notes.urls')),
    path('login/', notes_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', notes_view.register, name='register'),
    path('note/', notes_view.save_note, name='save_form'),
]
