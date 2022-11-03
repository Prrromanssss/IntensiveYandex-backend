# Django homework


## ![flake8 test](https://github.com/Prrromanssss/LyceumYandex_django/actions/workflows/python-package.yml/badge.svg)



## Deployment instructions


### 1. Cloning project from GitHub

1.1 Run this command
```commandline
git clone https://github.com/Prrromanssss/LyceumYandex_django.git
```

### 2. Creation and activation venv

2.1 First of all, from root directory run this command
```commandline
python -m venv venv
```
2.2 Then run this command to activate venv
#### Mac OS / Linux
```commandline
source venv/bin/activate
```
#### Windows
```commandline
.\venv\Scripts\activate
```

### 3. Installation all requirements

3.3 Run rhis command 
```commandline
pip install -r requirements.txt
```

### 4. Generete file with virtual environment variables (.env)

4.1 Generate file '.env' in root directory with structure specified in the 'examples/env_example.txt' file

### 5. Making migrations

5.1 To make migrations run this command

```commandline
python lyceum/manage.py makemigrations
```
5.2 To apply your migrations run this command
```commandline
python lyceum/manage.py migrate
```

### 6. Database setup

#### The first way
6.1.1 The example of the database you can see in the 'examples/example_db.sqlite3' file
6.2.1 Copy this database to 'lyceum/db.sqlite3'

#### The second way
6.1.2 To load data from the fixtures run this command
```commandline
python lyceum/manage.py loaddata data.json
```

### 7. Authorizing admin user

#### The first way
7.1.1 If you have copied example database you have already authorizing admin user
```commandline
Username: admin
Password: 12345
```

#### The second way
7.1.2 If you have loaded data from the fixtures run this command to authorize admin user
```commandline
python lyceum/manage.py createsuperuser
```
7.2.2 Write username and password for admin user

7.3 After running project you can access admin page by following '127.0.0.1:8000/admin' or 'localhost:8000/admin'

### 8. Running project

8.1 Run this command
```commandline
python lyceum/manage.py runserver
```
8.2 After running server follow link
'127.0.0.1:8000/admin' or 'localhost:8000/admin'


***

## ER-diagram
![Image of the ER-diagram](https://github.com/Prrromanssss/LyceumYandex_django/raw/main/media/ER-diagram.png)

***
