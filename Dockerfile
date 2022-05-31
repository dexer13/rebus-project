FROM python:3.10

COPY . /app
WORKDIR /app

# ENV VARS
ENV DEBUG=True
ENV SECRET_KEY="django-insecure-jzv^i=#=b0-e2c&y%#p^a(r_j_*7z0$1xwza%(+5fciibs(cv*"

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false --local
RUN poetry install

# Command run server with manage.py
CMD python3 manage.py runserver 0.0.0.0:8000
