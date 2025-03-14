FROM python:3.11-slim

WORKDIR /app

# Install system dependencies needed for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx libgtk2.0-0

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# We can remove this line for development with volumes

