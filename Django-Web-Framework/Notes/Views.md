# Views
## Views
### Views
- View creates the logic to present data to the end user
- <img width="768" alt="Screenshot 2023-08-23 at 5 29 30 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/5290593f-c075-4ce0-8180-e441ca53f7c5">
- Function designed to handle web requests and return a web response, **such as an HTML document**
  <img width="532" alt="Screenshot 2023-08-23 at 5 31 40 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/9697298f-d15c-4035-b6e1-9a5bc22bae59">
  - Each view function takes an HTTP request as its first parameter
- Views can process data, retrieve data, transform data, and render templates
- Needs to be mapped to a URL (**urls.py** at the _app level_), known as **routing**
  <img width="302" alt="Screenshot 2023-08-23 at 5 39 53 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/b9f59b5e-dab8-410f-8cfa-fb3cf77329df">
### Creating views and mapping to URLs
- **urls.py** exists in both the project and app level
- When requests are made, they are handled at the project level. Django looks for _url_patterns_.
- **include()** tells Django where to look at the app level .urls
  <img width="686" alt="Screenshot 2023-08-23 at 6 37 04 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/40127d8c-e2b7-427c-9437-e65f3966c5e0">
- When making a **app level urls.py**
  - import path from django.urls _and_ views from .
  - add a comma to match the parsing that django needs like _path('',views.home),_
  - in the **project urls.py** import **include** and pass the location
    <img width="209" alt="Screenshot 2023-08-23 at 6 43 25 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/a05dd9aa-6289-4d21-b581-2ed224d7c29e">
### View Logic
- View fetches data from the client's request and applies processing logic to it
- Receives data in the object of class HttpRequest
- **Models** are equivalent of a database in Djando
- View fetches objects from the model such as a datable table mapped with the model, or the request parameter is used to add a new instance of the model by inserting a new row in the table.
- Client uses **HTTP GET** to provide data from the model or delete an instance
- View loads the template web page, inserts certain context data at the placeholder marked with tags, and returns it as the response
  - **GET** and **POST** methods (in views)
    - You want to let the end user know about the result
- **Request** is requesting information from the server via code, **Response** is returning  to the server
### C

## Requests and URLs
-
-
-
## Creating URLs and Views
### Regular expressions in URLs
- Developers create one page whose content updates dynamically based on what's in the content in the URL
- **RegEx** is a set of characters that specify a pattern to search for within a string
  - __**from django.url import path, re_path**__
  - All URLs are accepted that meet the regex requirements
    <img width="607" alt="Screenshot 2023-08-23 at 12 36 46 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/af9ca129-0f03-4ef1-a1b5-7f5120a02d9e">
  - **^** is the beginning, **$** is the ending of the string **[]** matches a character set, **{}** amount of characters, **()** grouping parts of the RegEx
### URL Namespacing and Views
- **urls.py** contains a list of URL patterns for the app, each argument is a path string with the view function mapped to it and _optional_ argument name
- This is a **urls.py**
  <img width="363" alt="Screenshot 2023-08-23 at 12 48 43 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/2efb5e93-c182-4841-89da-3682c3bb5d90">
- An example of **/demoapp/login**
  <img width="358" alt="Screenshot 2023-08-23 at 12 50 20 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/a0ee5f8c-924b-47ff-9246-2cca8f0cfc95">
- **reverse()** function returns the URL path to which it is mapped to. Run _ python manage.py shell_
  <img width="288" alt="Screenshot 2023-08-23 at 12 54 45 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/5f0089eb-2a3c-4344-befe-5c26350a81de">
- **Application namespace** is _app_name_ = 'demoapp' and giving it the name of the app. In this instance, it's _demoapp/urls.py___
  <img width="328" alt="Screenshot 2023-08-23 at 12 58 33 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/2919b438-a348-4844-9edc-a786b38894f9">
  <img width="227" alt="Screenshot 2023-08-23 at 12 58 46 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/a57d5861-04d8-4264-ad35-c1c3e39bd5e9">
- Update the project **urls.py**
  <img width="360" alt="Screenshot 2023-08-23 at 1 01 22 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/385e7684-1c9e-44be-9a1c-64f089f204c7">
  - The reverse function called on the newapp
    <img width="220" alt="Screenshot 2023-08-23 at 1 01 38 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/b3360730-7a5f-4c3a-8b7a-8e59dd2c9a30">
  - **instance namespace** may also be used
    <img width="525" alt="Screenshot 2023-08-23 at 1 02 54 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/cf34b328-9c80-4fe7-b7c2-f17e0d3db088">
- **namespace in the URL tag**
  - An HTML form is submitted to the URL specified in the action module
  - _'demoapp:login'_ may be used aswell
    <img width="380" alt="Screenshot 2023-08-23 at 1 07 07 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/9a792118-f6b1-4098-a862-fc58fc66238c">
    <img width="620" alt="Screenshot 2023-08-23 at 1 07 42 PM" src="https://github.com/pabloisaiahs/meta-back-end-certificate/assets/85268281/7bb1fbaa-782b-4376-bf0b-966c6870828e">


