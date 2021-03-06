FROM python:3.10.5-alpine3.16
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# ENV DJANGO_ALLOWED_HOSTS = ${DJANGO_ALLOWED_HOSTS} 
# ENV DJANGO_DEBUG = ${DJANGO_DEBUG}
# ENV DJANGO_SECRET_KEY = ${DJANGO_SECRET_KEY}


WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
