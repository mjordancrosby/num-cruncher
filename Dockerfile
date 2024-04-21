FROM python:3.12-slim

WORKDIR /app

COPY compute .

COPY lib/__init__.py lib/__init__.py

RUN chmod +x compute

RUN useradd -m compute

RUN chown -R compute:compute /app

USER compute

ENV PATH="/app:${PATH}"
