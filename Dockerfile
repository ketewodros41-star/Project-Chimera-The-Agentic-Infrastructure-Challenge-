# Stage 1: Base & Dependencies
FROM python:3.12-slim AS base

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    make \
    && rm -rf /var/lib/apt/lists/*

# Cache Specs first (rubric requirement)
COPY specs/ /app/specs/

# Stage 2: Test Environment
FROM base AS test
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --extra dev

# Copy rest of the code
COPY . .

# Run as non-root user
RUN useradd -m agent
USER agent

# Default command
CMD ["make", "test"]
