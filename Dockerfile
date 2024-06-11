FROM python:3.10-slim

COPY src/ /src/
COPY pyproject.toml /
COPY .env /

RUN pip install poetry
RUN poetry install

CMD poetry run python src/main.py