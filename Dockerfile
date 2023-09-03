# Create docker image for the application
# Build: docker build -t <image-name> .

FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run controller.py when the container launches
CMD ["python", "-m", "src.run"]



