FROM python:3.7.10-slim

#Install missing required packages
RUN apt update && \
    apt install --yes libldap2-dev libsasl2-dev && \
    apt install --yes gcc

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
# Install requirements and upgrade pip package
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]