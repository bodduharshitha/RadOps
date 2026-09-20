FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir --upgrade --force-reinstall \
        "setuptools>=78.1.1" \
        "msgpack>=1.2.1" \
    && python -c "import setuptools; print('setuptools:', setuptools.__version__)" \
    && python -m pip check

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]