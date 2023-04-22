# Follow Task-0 subtask-1
# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt \ 
    && rm -rf /var/cache/apk/*

COPY ./app /app

EXPOSE 5050
CMD [ "python", "app.py" ]