FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Bring the system up to date
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install uv
ENV PATH="/root/.local/bin:${PATH}"
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy toml and lock
COPY pyproject.toml .
COPY uv.lock .

# Install project dependencies
RUN uv sync --locked

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]