# [Fix] Use a specific version tag for reproducibility instead of floating '3.12-slim'
FROM python:3.12.1-slim

# Set the environment variable for the port
ENV PORT 8080

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the working directory
# [Note] Ensure you have a .dockerignore file to exclude .env, .git, etc.
COPY . .

# [Fix] Create a non-root user and switch to it for security
# Create a system group and user 'appuser'
RUN addgroup --system appuser && adduser --system --group appuser

# Change ownership of the application directory to the new user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Command to run the application using Gunicorn
# Gunicorn is a production-ready WSGI server.
# [Fix] Changed --timeout 0 (infinite) to 120 seconds to prevent hanging
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 120 app:app
