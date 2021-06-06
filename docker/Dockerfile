FROM python:3.7

RUN apt-get update \
    && pip install pipenv

COPY src/ /usr/lib/

WORKDIR /usr/lib

RUN pipenv install

# CMD pipenv run python -m unittest discover
WORKDIR /usr/lib/carrier
CMD pipenv run python run.py