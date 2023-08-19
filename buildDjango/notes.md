## Project and Apps
Creating your first project
- Each project needs its own environment by using virtual development environments.
- Workflow:
  - Create project directory -> Create Virtual environment -> Create Django project -> Run development server
- **mkrdir whatever** then **cd** into it
- **python -m venv anyname-env** then **source anyname-env/bin/activate** to set it as the environment
- install Django by **pip3 install django**
- to make a project do **django-admin startproject projectName**
  - **manage.py** is a command line utility that works like the **django-admin** command
- to make the server do **python manage.py runserver**
# Admin and structures
Django-admin & manage.py commands
- **django-admin** admin ready utility task in the scripts folder
  - on system path
- **manage.py** is a local version located within project folder, points to settings.py
  - automatically created each time you start a project, venv specific
- You don't need to restart the server every time you update something, however, a file change might be an exception
## App Structures
A Django project is a web application that may consist of one or more sub-modules called apps
- An app performs one single task out of the many involved
- **python manage.py startapp myapp** default dest in cwd
- **views** receive requests and return a response by giving the user something
  - Uses HTTP request and response
- add to **views.py**, don't modify it
  - **from django.http import HttpResponse**
- go to **url.py** and **from myapp import views**
  - add the file path to the list, it executes on the home page if you do '' instead of admin
  - give it a **name = home** or anything
