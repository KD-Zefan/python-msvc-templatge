# FastAPI Microservice Template

This repository provides a template for building microservices using FastAPI, PostgreSQL, Docker, and Docker Compose. It is designed as a starting point for new microservices, providing a structured framework that can be easily extended with your own APIs and business logic.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **PostgreSQL**: A powerful, open-source relational database.
- **Docker & Docker Compose**: Simplifies containerized development and deployment.
- **Continuous Integration**: Supports static code analysis with Pylint via GitHub Actions.

## Tech Stack

- **FastAPI**: For building asynchronous web applications and APIs.
- **PostgreSQL**: For relational database management.
- **Docker**: Containerizes the application for local development and production environments.
- **Docker Compose**: Orchestrates multi-container setups, making it easy to run PostgreSQL and FastAPI together.
- **Pylint**: For ensuring code quality with static analysis.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)
- Python (if you want to develop and test outside Docker)

## Setup Instructions

Follow the steps below to set up and run the project on your local machine.

### 1. Clone the Repository

### 2. Create a .env File

A sample .env.example file is provided. Copy this to .env and adjust the values for local development.

```
cp .env.example .env
```

Update the .env file with appropriate values:

```
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/mydatabase
SECRET_KEY=mysecretkey
ENVIRONMENT=local
```

### 3. Build and Run the Application Using Docker Compose

You can use Docker Compose to build and run the application, along with a PostgreSQL database, locally.

```
docker-compose up --build
```

This will:

- Pull the necessary Docker images.
- Build the FastAPI service.
- Start both the FastAPI app and PostgreSQL database.

### 4. Running the Service

Once the services are running, you can access the FastAPI application via:

```
http://localhost:8000
```

You can also access the automatically generated API documentation:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

### 5. Database Management

The PostgreSQL database is exposed on port 5432. You can connect to it using any PostgreSQL client, such as psql or pgAdmin.

```
Host: localhost
Port: 5432
Database: mydatabase
Username: myuser
Password: mypassword
```
These values are configured in the .env file.

### 6. Stopping the Application

To stop the containers, run:

```
docker-compose down
```

This will stop and remove the containers but keep the data in the Docker volume.

### 7. Running Tests

Unit tests are included in the project and can be run inside the Docker container. First, make sure the containers are running, then execute the tests:

```
docker exec -it user-management-service_app_1 pytest
```

### 8. Additional Docker Commands

Rebuild the containers:

```
docker-compose up --build
```

Check running containers:

```
docker ps
```

### 8. Running Pylint Code Analysis

Pylint is set up to run automatically on each push via GitHub Actions. You can also run Pylint locally:

Install Pylint if it's not already installed:

```
pip install pylint
```

Run Pylint:

```
pylint $(git ls-files '*.py')
```
