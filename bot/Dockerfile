FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

ENTRYPOINT ["python3"]
CMD ["src/main.py"]
