from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm

from notes.models import Note


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']


class CreateNoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['title',  'content']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields =['title',  'content']