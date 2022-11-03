# Django homework


## ![flake8 test](https://github.com/Prrromanssss/LyceumYandex_django/actions/workflows/python-package.yml/badge.svg)


This project is a repository for Django intensive homework from the Yandex Academy.

***

### Deployment instructions

## 1 Cloning project from GitHub

1.1 Run this command
```commandline
git clone https://github.com/Prrromanssss/LyceumYandex_django.git
```

## 2 Creation and activation venv

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

## 3 Installation all requirements

3.3 Run rhis command 
```commandline
pip install -r requirements.txt
```

## 4 Generete file with virtual environment variables (.env)

4.1 Generate file '.env' in root directory with structure specified in the 'examples/env_example.txt' file

## 5 Making migrations

5.1 To make migrations run this command

```python
python lyceum/manage.py makemigrations
```
5.2 To apply your migrations run this command
```python
python lyceum/manage.py migrate
```

* load test data to databases
```commandline
python lyceum/manage.py loaddata data.json
```

* run server
```commandline
python lyceum/manage.py runserver
```

* you can see models in administration of Django. Go over 127.0.0.1:8000/admin

Login: admin

Password: 12345

***

## ER-diagram
![Image of the ER-diagram](https://github.com/Prrromanssss/LyceumYandex_django/raw/main/media/ER-diagram.png)

***
