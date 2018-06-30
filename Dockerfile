FROM python:3

RUN mkdir /app
WORKDIR /app
COPY django_app /app
RUN pip install -r requirements.txt