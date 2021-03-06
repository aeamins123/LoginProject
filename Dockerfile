FROM ubuntu:latest

MAINTAINER <aeamins> <aeamins@gmail.com>

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential python3

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ['python']

CMD ['app.py']

EXPOSE 5000