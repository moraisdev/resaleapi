
FROM python:3.6.10-alpine3.10 as base

RUN \
  apk update && \
  apk add bash py-pip && \
  apk add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev make && \
  pip --no-cache-dir install -U pip && \
  apk add make && \
  apk del --purge build

RUN apk add --update \
    supervisor \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    postgresql-dev \
    gcc

RUN easy_install bson
RUN apk add --no-cache pcre curl

COPY ./requirements.txt /requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /src
COPY ./code/src /src

FROM base as test
RUN pip install pytest pytest-cov pytest-flask
WORKDIR /
COPY ./code/tests /tests
CMD python -m pytest --cov-report term-missing --cov-report html --cov-report xml --cov=src tests/ --disable-pytest-warnings

FROM base as deploy
EXPOSE 80
CMD python3 uwsgi.py