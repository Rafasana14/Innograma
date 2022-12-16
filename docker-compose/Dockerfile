FROM python:3.10.6
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install ipdb
RUN pip install ipython
RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt
# Copy the Django project
COPY ./innograma /app/