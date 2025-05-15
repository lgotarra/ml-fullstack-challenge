FROM python:3.13-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set the working directory
WORKDIR /app

# Copy the application source
COPY . /app

# Install dependencies
RUN uv sync --frozen --no-cache

# Expose port
EXPOSE 8000

# Run the application
CMD ["/app/.venv/bin/fastapi", "run", "api/main.py", "--port", "8000", "--host", "0.0.0.0"]
