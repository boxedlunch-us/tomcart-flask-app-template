FROM python:3.6.1-alpine

MAINTAINER Ricky Nelson "rnelson@thetomcart.com"

#ENV COLOR=
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python","app.py"]
