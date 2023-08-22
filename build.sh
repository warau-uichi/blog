#!/usr/bin/env bash
# exit on error
set -o errexit

cd blog_api

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --username admin --email dummy@test.com --noinput