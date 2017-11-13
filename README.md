# hwpw

## Install Packages.
pip install djangorestframework

## Migration

### Create migration.
python manage.py makemigrations sms

### Show SQL statement.
python manage.py sqlmigrate sms 0001

### Install Tables.
python manage.py migrate
