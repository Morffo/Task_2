[![Pipeline Status](https://gitlab.crja72.ru/django_2023/students/149321-abdul.suleymanov05-mail.ru-47231/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django_2023/students/149321-abdul.suleymanov05-mail.ru-47231/badges/main/pipeline.svg)

# Запуск проекта в dev-режиме

## Технологии
- *Django 4.2*

## Использование


### Клонирование репозитория
- Для того, чтобы получить доступ к файлам репозитория необходимо скопировать его с помощью:
```commandline
   git clone git@gitlab.crja72.ru:django_2023/students/149321-abdul.suleymanov05-mail.ru-47231.git
   ```
- А затем перейти в каталог репозитория:
```commandline
   cd 149321-abdul.suleymanov05-mail.ru-47231
   ```


### Установка виртуального окружения
- Создаем виртуальное окружение с помощью: 
```commandline
   python -m venv venv
   ```
- А затем, Находясь в той же директории, активируем его:
```commandline
   source venv/bin/activate
   ```

#### Установка и классификация зависимостей
- requirements/dev.txt: Зависимости для разработки 
- Установка:
```commandline
   pip install -r requirements/dev.txt
```
- requirements/prod.txt: Зависимости для запуска(Основные)
- Установка: 
```commandline
   pip install -r requirements/prod.txt
```
- requirements/test.txt: Зависимости для тестирования
- Установка:
```commandline
   pip install -r requirements/test.txt
```


### Запуск 
- Переходим в каталог lyceum и запускаем проект:
```commandline
  cd lyceum
  python manage.py runserver 
```


### P.S
- Все скрытые данные хранятся в .env


