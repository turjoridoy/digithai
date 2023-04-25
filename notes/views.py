from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializer import NoteSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, CreateNoteForm, NoteForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.exceptions import SuspiciousOperation


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]


def index(request):
    notes_q = Note.objects.all()
    user_id = request.user.id
    notes = notes_q.filter(created_by=user_id)
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


def create_note(request):

    if request.method == 'POST':
        noteform = CreateNoteForm(request.POST)
        noteform.instance.created_by = request.user
        if noteform.is_valid():

            noteform.save()

            messages.success(request, f'Your note saved successfully!')
            return redirect('index')
    else:
        noteform = CreateNoteForm()

    return render(request, 'user/create_note.html', {'noteform': noteform, 'title': 'note create here'})


def delete_note(request, drug_id):
    d = Note.objects.get(id=drug_id)
    d.delete()
    return redirect('/')


def note_update(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            messages.success(request, f'Your note edited successfully!')
            return redirect('index')
    else:
        form = NoteForm(instance=note)

    return render(request, 'user/edit_note.html', {'form':form, 'title': 'note edit here'})


def note_details(request, id):
    note = Note.objects.get(id=id)

    return render(request, 'user/detail_note.html', {
        'title': 'details',
        'notes': note
    })
