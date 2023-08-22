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
  - on the system path
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
# Web Frameworks and MVT
## What is a web framework
Allow for fast development, clean structure, change and modification, and code reusability
- Front-end is the part that the user interacts with
- Back-end is the part that runs on a webserver and contains a database
- Django is fast, feature-rich, secure, and highly scalable (allows data to be moved without too many changes in configuration)
- **Three-Tier Architecture (Modular)** splits the application into 3 logical parts
  - **Presentation tier** is the UI users interact with that communicates with other tiers.
  - **Data tier** stores and retrieves data, a database is then seen as the best viable
  - **Application Layer** gets data from the presentation tier and sends it to the data tier. Ties the two other tiers together
  <img width="843" alt="Screenshot 2023-08-21 at 4 41 44 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/32638e46-1e93-405d-8fe6-b07573405e89">
## MVT (Model, View, and Template)
- **Web Framework**
  - Software frameworks are reusable software to facilitate the rapid development of applications
  - Web application frameworks provide general functionality for web building, APIs and web services
      - Out-of-the-box support to operations and integration/templating
- **MVC Architecture** is a design pattern that separates the application development process into 3 layers, Model, View, Controller
  ![image](https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/ecdaf1ef-a50f-47f9-b2c0-8bcc17bb05ca)
  - The controller intercepts user requests
    - Coordinates with the view and model layers to send the appropriate response back to the client
  - The view is the presentation layer of the application
    - Takes care of the placement and formatting of the result and sends it to the controller which redirects it to the client as a response
- **MVT Architecture** (Model, View, and Template)
- ![image](https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/fa247d6c-b6b5-4875-90ff-3f2cfb47ec34)

  - Similar to MVC, the data layer contains the model and the view undertakes processing logic
    ![image](https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/07b01417-f394-4969-b482-5c4bae2fef1d)
    - A django application consists of the following components:
      - URL Dispatcher,View, Model, and Template
- **URL Dispatcher**
  - Django's URL dispatcher mechanism is equivalent to the controller in MVC
  - The **urls.py** module acts as a dispatcher.
    - Provides URL patterns. Each URL pattern is mapped with a view function invoked when the client's request URL is matched. Here is _url.py_
    <img width="374" alt="Screenshot 2023-08-22 at 11 46 53 AM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/552d5827-a0c8-4d37-92da-52b422baf916">
  - When the server receives a request in the client URL, the dispatcher matches its pattern with the patterns available in the urls.py and then routes the flow
- **View**
  - Reads the path, query, and body parameters from client's requests and uses the data to interact with the model to perform CRUD operations
    - _CRUD operations_ are to create, read, update, and delete are the four basic operations of persistent storage
  - Can be a user-defined function or class
  - You create view definitions in the **views.py** file of the respective app folder
  - _The following code in view.py file defines the index() view function_
    <img width="383" alt="Screenshot 2023-08-22 at 11 52 23 AM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/b6cdb1c5-9591-4f71-898a-c4b82759d7fd">
- **Model**
  - An app may have one or more model classes, in the **models.py** file
  - Django migrates attributes of the moedl class to construct a database table of a matching structure
  - Django's Object Relational Mapper helps perform CRUD operation in an OOP way instead of invoking SQL queries
  - View uses client's and the model's data and renders its response using a template
- **Template**
  - Web page containing a mix of static HTML and Django language code blocks
  - Template web pages are placed in the templates folder with an _.html_ exnteion
  - Django's template processor uses any contect data from the view inserted in these blocks to formualte a dyanimc response.
  - The view, in turn, returns the response to the user
