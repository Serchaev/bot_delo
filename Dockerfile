FROM python:3.10

RUN mkdir app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry


COPY poetry.lock pyproject.toml .
RUN poetry install --no-dev

COPY . /app/

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run python main.py"]