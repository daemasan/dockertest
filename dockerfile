FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN apt-get update -y && apt-get install -y gcc libc-dev default-libmysqlclient-dev
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 config.wsgi:application
CMD python manage.py runserver --settings config.env.dev 0.0.0.0:8080