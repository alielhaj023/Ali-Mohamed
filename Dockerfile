# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy the application files
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Set build arguments for sensitive environment variables
ARG ENV_FILE=.env
RUN if [ -f "$ENV_FILE" ]; then export $(grep -v '^#' $ENV_FILE | xargs); fi


# Expose the port
EXPOSE 8000

# Run Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
