FROM python:3.10

WORKDIR /src
COPY poetry.lock /src
COPY pyproject.toml /src
RUN pip install poetry
RUN poetry install
COPY . /src
ENTRYPOINT ["poetry", "run", "python", "src/main.py"]
