#!/usr/bin/env bash
# exit on error
set -o errexit

cd blog_api

pip install -r requirements.txt

python manage.py collectstatic --noinput
echo "done collectstatic"
python manage.py migrate
echo "done migrate"
python manage.py createsuperuser --username dummyiki123 --email dummy@test.com --noinput
echo "done createsuperuser"