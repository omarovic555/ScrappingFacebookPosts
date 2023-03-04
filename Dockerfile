# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the local source directory to the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Define environment variable
ENV DATABASE_URL="sqlite:///mydatabase.db"

#  Specifies the default command to be run when a container is started from the image. 
CMD ["python", "app.py"]

