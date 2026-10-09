FROM python:3.8-slim

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copiar archivos de proyecto e instalar dependencias con uv
COPY pyproject.toml .
RUN uv pip install --system -r pyproject.toml

COPY app.py .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
