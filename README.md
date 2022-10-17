# YaMDb project

«Composition reviews»

## Description

The project collects user reviews of the works. The works are divided into categories of books, films and music.

## Technologies

    Python==3.7.9
    requests==2.26.0
    django==2.2.16
    djangorestframework==3.12.4
    djangorestframework-simplejwt==4.7.2
    PyJWT==2.1.0
    pytest==6.2.4
    pytest-django==4.4.0
    pytest-pythonpath==0.7.3
    django-filter~=21.1

## Dev-mode running

Install dependencies from the file requirements.txt

    pip install -r requirements.txt

In the file folder manage.py run the command:

    python manage.py runserver

## Documentation with sample requests is available at:

    http://127.0.0.1:8000/redoc/

## Self-registration of new users:

The user sends a POST request with the email and username parameters to the endpoint
   
    /api/v1/auth/signup/

The service sends an email with a confirmation code to the specified address.

The user sends a POST request with the username and confirmation_code parameters to the endpoint

    /api/v1/auth/token/

In response to the request, a token is received, which must be passed in the header of all requests with the Bearer parameter

After registering and receiving the token, the user can send a PATCH request to the endpoint
    
    /api/v1/users/me/ 

and fill in the fields in your profile

## Creating a user by an administrator

The user can be created by the administrator — through the admin zone of the site or through a POST request for a special endpoint

    api/v1/users/

(the description of the request fields for this case is in the documentation). At this point, the user does not need to send an email with a confirmation code.
After that, the user must independently send his email and username to the endpoint

    /api/v1/auth/signup/

in response, he should receive an email with a confirmation code.
Next, the user sends a POST request with the username and confirmation_code parameters to the endpoint

    /api/v1/auth/token/

in response to the request, he receives a token (JWT token), as with self-registration.

## Request examples


The API is available at URL

    GET..../api/v1/

API request parameters:

Example of a POST request with an Administrator token (Only an administrator can add and make changes to categories, reading is available to any unregistered user): 

Adding a new category:

    POST .../api/v1/categories/

    {
        "name": "string",
        "slug": "string"
    }

Answer:
    
    {
        "name": "string",
        "slug": "string"
    }

Example of a POST request with an Administrator token (Only an administrator can add and make changes to genres, reading is available to any unregistered user):

Genre adding:

    POST .../api/v1/genres/

    {
        "name": "string",
        "slug": "string"
    }

Answer:

    {
        "name": "string",
        "slug": "string"
    }

Example of a POST request with an Administrator token (Only an administrator can add and make changes to works, reading is available to any unregistered user):

Adding a work:

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

Answer:

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


Example of an unregistered user's GET request (without a token):

We get a list of all the works /genres/ categories of 5 on the page.

    GET .../api/v1/titles/
    GET .../api/v1/genres/
    GET .../api/v1/categories/

Answer (for compositions):

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
    


Authors __Pavel Kalinin__, __Marina Buzina__, __Vitaly Ostashov__
