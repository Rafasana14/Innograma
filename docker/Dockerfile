FROM python:3.10.6
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app/innograma
# Install dependencies
RUN pip install --upgrade pip

COPY requirements.txt /app/innograma

RUN pip install -r requirements.txt
# Copy the Django project
COPY ./innograma /app/innograma

EXPOSE 8000

ENTRYPOINT ["python", "manage.py","runserver","0.0.0.0:8000","--settings=Innograma.settings.local"]