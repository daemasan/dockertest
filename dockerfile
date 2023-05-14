FROM python:3.11-slim
ARG _SETTINGS_MODULE
ENV SETTINGS_MODULE ${_SETTINGS_MODULE}
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN apt-get update -y && apt-get install -y gcc libc-dev default-libmysqlclient-dev
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD exec gunicorn --env DJANGO_SETTINGS_MODULE=$SETTINGS_MODULE --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 config.wsgi:application