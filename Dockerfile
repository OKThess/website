FROM python:3.6.1
ENV PYTHONUNBUFFERED 1
RUN apt-get update

RUN apt-get install -y swig libssl-dev dpkg-dev netcat
RUN pip install -U pip
ADD requirements.txt /code/
RUN pip install -Ur /code/requirements.txt

ADD CHECKS /app/
ADD * /code/

WORKDIR /code
COPY . /code/
RUN /code/manage.py collectstatic --noinput
