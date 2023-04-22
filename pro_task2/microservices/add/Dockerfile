# Use an appropriate base image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY ./app/requirements.txt /app/requirements.txt

# Install dependencies
RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

# Copy the application code
COPY ./app /app

# Expose the required port
EXPOSE 5051

# Run the Flask application
CMD ["python3", "app.py"]


