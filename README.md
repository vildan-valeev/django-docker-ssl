# docker-django-ssl

Template for dockerizing django project with ssl cert (https).

Before RUN, you need to replace site.ru and email in init-ssl.sh and settings.py

`chmod +x init-ssl.sh`

`./init-ssl.sh`

`docker-compose up --build`