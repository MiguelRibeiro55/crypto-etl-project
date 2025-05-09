# Use a Python 3.13 base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies and Netcat (netcat-openbsd) to allow the wait-for-it.sh script to work
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the local files to the container
COPY . /app

# Copy the wait-for-it.sh script into the container
COPY wait-for-it.sh /usr/src/app/wait-for-it.sh

# Make the script executable
RUN chmod +x /usr/src/app/wait-for-it.sh

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run when the container starts
CMD ["python", "src/main.py"]
