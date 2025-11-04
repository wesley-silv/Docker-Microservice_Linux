# Multi-stage: build stage
FROM python:3.11-slim as build

# Install build deps separately and then remove them to keep image small
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy only what is necessary to install deps
COPY services/auth/pyproject.toml services/auth/poetry.lock* /app/
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-interaction

# App code
COPY services/auth/app /app

# Final minimal runtime image
FROM python:3.11-slim

# Create non-root user
RUN groupadd -g 1000 appgroup && useradd -u 1000 -g 1000 -m appuser

# Copy deps from build stage
COPY --from=build /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /app /app

WORKDIR /app

# Give non-root ownership
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
