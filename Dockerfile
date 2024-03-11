# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install stanza library
RUN pip install stanza

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY pos_tagging.py /app/

# Run the Python script when the container launches
CMD ["python", "pos_tagging.py"]
