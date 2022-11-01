# Django homework


## ![flake8 test](https://github.com/Prrromanssss/LyceumYandex_django/actions/workflows/python-package.yml/badge.svg)


This project is a repository for Django intensive homework from the Yandex Academy.

***
To __start__ it we need:
* clone project from GitHub
```commandline
git clone https://github.com/Prrromanssss/LyceumYandex_django.git
```
* set virtual environment
### Mac OS / Linux
```commandline
python -m venv venv
source venv/bin/activate
```
### Windows
```commandline
python -m venv venv
.\venv\Scripts\activate
```


* install all requirements
```commandline
pip install -r requirements.txt
```
* generate a '.env' file with environment variables. Its structure is presented in the file 'env_example.txt'

* migrate our databases
```commandline
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




## ER-diagram
![Image of the ER-diagram](https://github.com/Prrromanssss/LyceumYandex_django/raw/main/media/ER-diagram.png)

***
