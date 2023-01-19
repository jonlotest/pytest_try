FROM python:3.8-alpine

LABEL 'course' = 'testing'
LABEL 'creator' = 'jonlo'pip

WORKDIR ./usr/lessons

COPY . .

RUN apk update && upgrade apk add bash

RUN pip3 install -requirements.txt

CMD pytest -s -v Tests/*