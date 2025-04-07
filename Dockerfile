# Based on https://fastapi.tiangolo.com/deployment/docker/#containers-with-multiple-processes-and-special-cases

FROM python:3.13

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install fastapi[standard] && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./tests/test_database.csv /code/tests/test_database.csv

CMD ["fastapi", "run", "app/main.py", "--port", "80", "--workers", "4"]