# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy requirements and install
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Expose the container’s port for the Flask app
EXPOSE 5000

# Define the command to run the app
CMD [ "python", "main.py" ]
