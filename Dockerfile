# Dockerfile

# Using Python base image version 3.11
FROM python:3.11

# Update system packages and install necessary dependencies
RUN apt-get update && apt-get install -y gcc unixodbc-dev

# Install ODBC driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Upgrade pip
RUN pip install --upgrade pip

# Create working directory /app
WORKDIR /app

# Copy all project files to the working directory
COPY . /app

# Install project dependencies from requirements.txt
RUN pip install -r requirements.txt

# Set the command to run the project using uvicorn
CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "80"]