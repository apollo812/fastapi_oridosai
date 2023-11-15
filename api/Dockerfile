# Use the specified base image
FROM nginx/unit:1.28.0-python3.10 as base

# Set the default project name
ARG PROJECT=api

# Create a non-root user to run the app with.
RUN groupadd --gid 1000 user && adduser --disabled-password --gecos '' --uid 1000 --gid 1000 user

# Switch to the user
USER user

# Set the working directory
WORKDIR /home/user

# Install Poetry.
RUN --mount=type=cache,target=/home/user/.cache pip install --user poetry==1.4.2

# Set environment variables
ENV PATH="/home/user/.local/bin:/home/user/.venv/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# Copy the project files and configuration
COPY --chown=user:user ./pyproject.toml ./poetry.lock ./
COPY --chown=user:user ./config/config.json /docker-entrypoint.d/config.json

# Install dependencies
RUN --mount=type=cache,target=/home/user/.cache poetry install

# Development stage
FROM base as dev

# Copy the project files
COPY --chown=user:user ./$PROJECT /home/user/$PROJECT

# Expose the application port
EXPOSE 5000

# Test stage
FROM base as test

# Install development dependencies
RUN --mount=type=cache,target=/home/user/.cache poetry install --with dev

# Copy the project files
COPY --chown=user:user ./$PROJECT /home/user/$PROJECT

# Create a mypy cache directory
RUN mkdir /home/user/.mypy_cache && chown -R user:user /home/user/.mypy_cache

# Default target stage
FROM dev
