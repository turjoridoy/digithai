from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase

from notes.models import Note


class NoteTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="admin77", password="1234")
        Note.objects.create(title="Note44", content="This is a new note", created_by=user)
        Note.objects.create(title="Note22", content="3",created_by=user)

    def test_note_that_exists(self):
        response = Note.objects.filter(title='Note44', content='a')
        self.assertEqual(len(response), 0)

    def test_user_that_exists(self):
        user = User.objects.create(username="admin7887", password="1234")
        self.assertEqual(user.username, "admin7887")

    def test_login(self):
        user = User.objects.filter(username="admin77", password="13234")

        # Checking this user already exists or not
        self.assertEqual(len(user), 0)





