FROM python:3.8

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements/* /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

