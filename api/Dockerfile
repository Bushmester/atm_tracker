FROM python:3.10

WORKDIR /src
COPY poetry.lock /src
COPY pyproject.toml /src
RUN pip install poetry
RUN poetry install
COPY . /src
WORKDIR /src/src
ENTRYPOINT ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

