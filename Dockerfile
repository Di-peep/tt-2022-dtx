# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD db.py .
ADD parser.py .
ADD config.py .

CMD [ "python", "parser.py"]