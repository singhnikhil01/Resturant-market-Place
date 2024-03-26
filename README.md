## Setting Up Django Environment

### 1. Create Virtual Environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 2. Create Virtual Environment:

```bash
django-admin startproject MyRestaurant .
```

### 3. To run the development server::

```bash
python3 manage.py runserver
```

### 4. To create a new app:

```bash
python3 manage.py startapp <name>
```

### 5. To create a superuser:

```bash
python3 manage.py createsuperuser
```

### 6. To create a new user:

```bash
python3 manage.py createuser <name>
```

### 7. To change a user's password:

```bash
python3 manage.py changepassword <username>
```

### 8. To create table migrations:

```bash
python3 manage.py makemigrations <name>
```

### 9. To apply migrations to the database:

```bash
python3 manage.py makemigrations <name>:
```

### 10. Install psycopg2 for PostgreSQL:

```bash
pip install psycopg2
```

### 11. Install python-decouple for managing passwords:

```bash
pip install python-decouple
```

## 12. Deploying the project

```bash
WSGI: Web Server Gateway Interface (e.g., Apache)
ASGI: Asynchronous Server Gateway Interface
URLs: Route53 server
Settings: All configuration settings
```

## Environments

```bash
SECRET_KEY=
# Database configuration settings
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
ALLOWED_HOST=
```
