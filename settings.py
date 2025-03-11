import os
from dotenv import load_dotenv # type: ignore

load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Postgre SQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mycrud',
        'USER': 'postgres',
        'PASSWORD':DB_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'crud',
)

SECRET_KEY = 'SECRET KEY for this Django Project'
