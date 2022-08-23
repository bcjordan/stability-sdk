FROM docker.io/python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
  libmagic1 \
  python3-magic \
  && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install git+https://github.com/benoitc/gunicorn.git
RUN pip3 install stability-sdk

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:80"
COPY . .

EXPOSE 80

CMD gunicorn app:app
