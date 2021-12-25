FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

ENV LISTEN_PORT 8080
EXPOSE 8080