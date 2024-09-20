# Use an official Python runtime as a parent image

FROM python:3.9-slim

# Set the working directory in the container

WORKDIR /usr/src/app

# Copy the requirements file to the container

COPY requirements.txt .

# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code

COPY . /app/

# Change directory to where manage.py is located
WORKDIR /app/op_crm_backend

# Expose the port on which Django will run

EXPOSE 8000

# Run Django development server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

