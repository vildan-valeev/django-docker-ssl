#!/bin/sh

python manage.py flush --no-input
python manage.py migrate
python3 manage.py collectstatic

exec "$@"
