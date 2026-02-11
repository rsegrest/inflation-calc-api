# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="${PYTHONPATH}:/app/src/"

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application using a production server like Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
