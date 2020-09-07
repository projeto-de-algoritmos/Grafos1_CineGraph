FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
