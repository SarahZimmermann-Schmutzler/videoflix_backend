# Stage 1: Build the dependencies in an isolated environment
#base image (specific to the app's requirements)
FROM python:3.12.2-slim AS builder

WORKDIR /app

# Install Git and PostgreSQL headers for psycopg2 (plus GCC to compile)
RUN apt-get update && apt-get install -y git gcc libpq-dev

# Copy only the requirements file to install dependencies
COPY requirements.txt $WORKDIR

# Upgrade pip and install dependencies
RUN pip install --upgrade pip -r requirements.txt --no-cache-dir

# Stage 2: Copy application files into a lightweight image
FROM python:3.12.2-slim

WORKDIR /app

# Copy only the installed dependencies from the builder stage
COPY --from=builder /usr/local /usr/local

# Copy the project files into the container
COPY . $WORKDIR

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the port for Nginx
EXPOSE 8000

# Use the entrypoint script to start the app
ENTRYPOINT ["/app/entrypoint.sh"]