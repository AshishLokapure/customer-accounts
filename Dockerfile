FROM python:3.10-slim

# Python runtime settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create a non-root user and writable database directory
RUN addgroup --system app && \
    adduser --system --ingroup app app && \
    mkdir -p /app/instance && \
    chown -R app:app /app

# Run as a non-root user
USER app

# Expose Flask application port
EXPOSE 8080

# Start the Customer Accounts Microservice
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]
