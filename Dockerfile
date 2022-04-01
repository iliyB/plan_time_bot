FROM python:3.9

ENV POETRY_VERSION=1.1.12
ENV TELEGRAM_API_TOKEN=""
ENV PYTHONPATH "${PYTHONPATH}:/app"
ARG ENV

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /app/

RUN apt-get update \
    && apt-get autoclean && apt-get autoremove \
    && apt-get install sqlite3 \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install $(if test "$ENV" = prod; then echo "--no-dev"; fi)
COPY bot/ /app/bot
WORKDIR /app/

ENTRYPOINT ["python", "bot/main.py"]