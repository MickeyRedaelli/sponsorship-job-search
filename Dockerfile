FROM python:3.12.4

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app