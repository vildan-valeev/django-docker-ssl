#!/bin/sh

python manage.py flush --no-input
python manage.py migrate --no-input
python3 manage.py collectstatic --no-input

exec "$@"
