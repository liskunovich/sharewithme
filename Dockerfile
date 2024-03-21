ARG PYTHON_VERSION

FROM python:$PYTHON_VERSION AS base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV ROOT /app
ENV PYTHONPATH "${PYTHONPATH}:/app/src/"

WORKDIR $ROOT

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install -y --no-install-recommends libc-dev \
  && apt-get install -y --no-install-recommends gcc \
  && apt-get install -y --no-install-recommends gettext \
  && apt-get install -y --no-install-recommends screen \
  && apt-get install -y --no-install-recommends vim \
  && apt-get clean

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry

RUN poetry config virtualenvs.create false

COPY src/pyproject.toml src/poetry.lock $ROOT/
RUN poetry install --no-root --no-dev

COPY commands $ROOT/commands
RUN chmod +x $ROOT/commands/*
ENV PATH="$ROOT/commands:$PATH"

ADD src $ROOT/src

WORKDIR $ROOT/src

CMD [ "start.sh" ]

