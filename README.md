create a virtual Environment
django-admin startproject MyResturant . // . to create in the root folder
python3 manage.py runserver //run the development server
python3 manage.py startapp < name> //will create a new app
python3 manage.py createsuperuser < name> //will create a new user
python3 manage.py createuser < name> //will create a new user
python3 manage.py changepassword < username name> //will change the password
python3 manage.py makemigrations < name> //will create the table migration
pythone manage.py migrate < name> //will add add in the database

WSGI webeserver gateway interface gateway //deploying the server to the projection server like apache
asgi : asynchronous server gateway //deploying the server to the
urls : Route53 server

settings : all the configuration settings

// Django follow MVT design patter , that is Model view and templated view
model - data base operations for
template - user facing templates
view - middle ware between the template and the model

// to add the bootstrap we need to Include the CDN to the project serer,
continiously delivery Network

psycopg2 to the project to use the sql database
pip install psycopg2
