# Проект YaMDb

«Отзывы на произведения»

## Описание

Проект собирает отзывы пользователей на произведения. Произведения делятся на категории книги, фильмы и музыка.

## Технологии

    Python 3.7
    requests==2.26.0
    django==2.2.16
    djangorestframework==3.12.4
    PyJWT==2.1.0
    pytest==6.2.4
    pytest-django==4.4.0
    pytest-pythonpath==0.7.3
    django-filter~=21.1

## Запуск проекта в dev-режиме

Установите зависимости из файла requirements.txt

    pip install -r requirements.txt

В папке с файлом manage.py выполните команду:

    python manage.py runserver

## Примеры запросов


Сам API доступен по адресу

    GET..../api/v1/

Примеры запросов к API:

Пример POST-запроса с токеном Администратора (Добавлять и вносить изменения в категории может только администратор, чтение доступно любому незарегистрированному пользователю): 

Добавление новой категории:

    POST .../api/v1/categories/

    {
        "name": "string",
        "slug": "string"
    }

Ответ:
    
    {
        "name": "string",
        "slug": "string"
    }

Пример POST-запроса с токеном Администратора (Добавлять и вносить изменения в жанры может только администратор, чтение доступно любому незарегистрированному пользователю): 

Добавление жанра:

    POST .../api/v1/genres/

    {
        "name": "string",
        "slug": "string"
    }

Ответ:

    {
        "name": "string",
        "slug": "string"
    }

Пример POST-запроса с токеном Администратора (Добавлять и вносить изменения в произведения может только администратор, чтение доступно любому незарегистрированному пользователю): 

Добавление произведения:

    POST .../api/v1/titles/

    {
        "name": "string",
        "year": 0,
        "description": "string",
        "genre": 
            [
                "string"
            ],
        "category": "string"
    }

Ответ:

    {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre":
            [
                {
                    "name": "string",
                    "slug": "string"
                }
            ],
        "category":
            {
                "name": "string",
                "slug": "string"
            }
    }


Пример GET-запроса незарегистрированного пользователя (без токена):

Получаем список всех произведений/жанров/категорий по 5 на странице.

    GET .../api/v1/titles/
    GET .../api/v1/genres/
    GET .../api/v1/categories/

Ответ (для произведений):

    [
        {
            "count": 0,
            "next": "string",
            "previous": "string",
            "results":
                [
                    {
                        "id": 0,
                        "name": "string",
                        "year": 0,
                        "rating": 0,
                        "description": "string",
                        "genre":
                            [
                                {
                                    "name": "string",
                                    "slug": "string"
                                }
                            ],
                        "category":
                            {
                                "name": "string",
                                "slug": "string"
                            }
                    }
                ]
        }

    ]
    


Авторы __Паша Калинин__, __Марина Бузина__, __Виталий Осташов__
