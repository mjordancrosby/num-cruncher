FROM python:3.12-slim

WORKDIR /app

COPY compute.py .

COPY scripts/compute .

RUN chmod +x compute

RUN useradd -m compute

RUN chown -R compute:compute /app

USER compute

ENV PATH="/app:${PATH}"