from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializer import NoteSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.exceptions import SuspiciousOperation


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]


def index(request):
    notes = Note.objects.all()
    return render(request, 'user/index.html', {
        'title': 'index',
        'notes': notes
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            d = {'username': username}

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'register here'})


def Login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})


def notes(request):
    if request.session.get('user'):
        user_id = request.session.get('user')
        if user_id is None:
            raise SuspiciousOperation("client_id is mandatory in query params")
        Note.objects.get(id = int(user_id))

        context = {
            'user': user_id,
            'status': 1,
        }
        return render(request, 'note.html', context)

    else:
        context = {
        }
        return render(request, 'login.html', context)


#
# def save_note(request):
#     if request.method == "POST":
#         form = Note(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = Note()
#     return render(request, 'user/note.html', {'form': form, 'title': 'register here'})
