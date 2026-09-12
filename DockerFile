# Use a lightweight, official Python image from Docker Hub
FROM python:3.11-slim

# Set up a secure working directory inside the container
WORKDIR /app

# Copy the Python file into the container
COPY app.py .

# Install Flask safely
RUN pip install --no-cache-dir flask

# Expose the network port your app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
