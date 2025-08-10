FROM python:3.12

WORKDIR /code

# Installeer netcat-openbsd vóór Poetry
RUN apt-get update && apt-get install -y netcat-openbsd

# Installeer Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Kopieer alleen dependency-bestanden (beter voor cache)
COPY pyproject.toml poetry.lock* /code/

# Installeer dependencies
RUN poetry install --no-root

# Kopieer volledige app
COPY . /code/

# Zet environment variables
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

# Zorg dat staticfiles map bestaat en static assets verzameld zijn in het image
RUN mkdir -p /code/staticfiles \
	&& poetry run python manage.py collectstatic --noinput

# Start de app via Poetry
CMD poetry run gunicorn blog_project.wsgi:application --bind 0.0.0.0:$PORT
