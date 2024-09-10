# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Set environment variables
ENV FLASK_APP=todo_app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 (Flask default)
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
