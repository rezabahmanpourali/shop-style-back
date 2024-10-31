# Use a base image with Python
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]