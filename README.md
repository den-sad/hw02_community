# Проект предназначен для закрепления навыков тестирования Django

## Запуск проекта

Склонируйте репозитарий

```
git clone git@github.com:den-sad/hw02_community.git
```

Создайте и активируйте виртуальное окружение

```
cd hw02_community
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

Запуск Django

```
python3 yatube\manage.py migrate
python3 yatube\manage.py createsuperuser
python3 yatube\manage.py runserver

```

## Запуск тестов

В коренвом каталоге выполните 

```
pytest
```