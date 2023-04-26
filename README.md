**DIGITHAI Assessment**

Installation instructions:

Clone the repo from github.

  		https://github.com/turjoridoy/digithai.git

**Run docker:**

    sudo docker-compose build
    sudo docker-compose run web python manage.py makemigrations
    sudo docker-compose run web python manage.py migrate
    sudo docker-compose up


**Web App:**

Now Browse: http://0.0.0.0:8000/

Signup: Goto Signup page from tab

    - Sign up with username and password (8 digits must)
    - Then go to login page and login with your credentials
    - After that home page showing your notes (currently empty as there is no note created by this user)
    - Click on "Create Note" to create a new note and fillup necessary entity.
    - Now if you go to home page you can see the notes by this user and from there you can delete and edit every note of yours.