FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

# Seguridad: crear usuario no-root y cambiar a él
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
