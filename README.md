# World Cup:
Rest services to manage world cup data.
***
## Índice
1. [Stack](#stack)
2. [Architecture](#architecture)
3. [File Structure](#file-structure)
4. [IDE](#ide)
5. [requirements](#requirements)
6. [Deployment](#deployment)
7. [Services](#services)
8. [Author](#author)
***
## Stack

  - [Django](https://www.djangoproject.com/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [Postgresql](https://www.postgresql.org/)
  - [Poetry](https://python-poetry.org/)
  - [Docker Compose](https://docs.docker.com/compose/)
  
***
## File Structure
```shell script
.
├── app
│   ├── asgi.py
│   ├── constants.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── world_cup
│   ├── admin
│   │   ├── __init__.py
│   │   ├── player_admin.py
│   │   ├── staff_admin.py
│   │   └── team_admin.py
│   ├── api
│   │   ├── v1
│   │   │   ├── serializers
│   │   │   │   ├── __init__.py
│   │   │   │   ├── player_serializer.py
│   │   │   │   ├── staff_serializer.py
│   │   │   │   └── team_serializer.py
│   │   │   ├── views
│   │   │   │   ├── base_views.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── meta_views.py
│   │   │   │   ├── resume_views.py
│   │   │   │   └── world_cup_views.py
│   │   │   ├── __init__.py
│   │   │   └── urls.py
│   │   └── __init__.py
│   ├── fixtures
│   │   ├── test
│   │   │   ├── players.json
│   │   │   ├── staff.json
│   │   │   └── teams.json
│   │   ├── players.json
│   │   ├── staff.json
│   │   └── teams.json
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models
│   │   ├── base_model.py
│   │   ├── __init__.py
│   │   ├── person_model.py
│   │   ├── player_model.py
│   │   ├── staff_model.py
│   │   └── team_model.py
│   ├── process
│   │   ├── base_process.py
│   │   ├── __init__.py
│   │   ├── player_process.py
│   │   ├── staff_process.py
│   │   └── team_process.py
│   ├── tests
│   │   ├── test_process
│   │   │   ├── __init__.py
│   │   │   ├── test_player_process.py
│   │   │   ├── test_resumen.py
│   │   │   ├── test_staff_process.py
│   │   │   └── test_team_process.py
│   │   └── __init__.py
│   ├── apps.py
│   ├── exceptions.py
│   └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md


```
***
## IDE
  - The project was developed with [PyCharm](https://www.jetbrains.com/es-es/pycharm/) con [licencia de estudiante](https://www.jetbrains.com/es-es/community/education/#students)
***
## Requirements
- Install **docker** and **docker-compose**
## Deployment
- Clone repository from GitHub
```shell script
git clone https://github.com/dexer13/rebus-project.git project
cd project
```
- Build project with docker compose
```shell script
docker-compose up --build
```
### First time
- Initialize the config file and migrations location
```shell script
docker-compose exec web python manage.py migrate
```
- Load seed data
```shell script
docker-compose exec web python manage.py loaddata teams.json players.json staff.json
```
- Create superuser to django admin username=admin, email=admin@example.com amd password=123 
```shell script
docker-compose exec web python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '123')"
```

***
## Tests
Run tests
```shell script
docker-compose exec web python manage.py test
```
***
### Servicios
Go to [http://localhost:8000/](http://localhost:8000/docs) to see all services
***
### Autor
The project was developed by:
 - Denis González [GitHub](https://github.com/dexer13) [LinkedIn](https://www.linkedin.com/in/denis-eduardo-isidro-gonzalez-428a51210/)

***
