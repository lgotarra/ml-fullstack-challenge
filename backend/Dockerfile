FROM python:3.13-slim-bookworm

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the application into the container.
COPY . /app

# Copy the environment variables.
COPY .env.deploy /app/.env

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Expose the port 8000 for the container
EXPOSE 8000
# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "api/main.py", "--port", "8000", "--host", "0.0.0.0"]