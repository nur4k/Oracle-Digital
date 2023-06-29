FROM python:3.11-slim as builder
WORKDIR /app
## Install poetry
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH=$PATH:/etc/poetry/bin

##
ADD ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main

FROM python:3.11-slim
WORKDIR /app
ENV PATH=/app/.venv/bin:$PATH PYTHONPATH=$PYTHONPATH:/app/
COPY --from=builder /app/.venv .venv
RUN mkdir -p media
RUN mkdir -p static
COPY . .
RUN python3 manage.py collectstatic --settings core.settings_test
ENTRYPOINT ["gunicorn", "core.wsgi", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "4"]
