# User Management Service

This is a microservice for user management, including user registration, authentication (using JWT), and profile management. It is built using FastAPI, PostgreSQL, Docker, and Docker Compose.

## Features

- **User Registration**: Create new users with hashed passwords.
- **User Authentication**: Secure login using JWT tokens.
- **Profile Management**: Fetch and update user profile information.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **PostgreSQL**: The relational database used to store user information.
- **Docker**: Used to containerize the application and database.
- **Docker Compose**: Orchestrates the containers for local development.

## Prerequisites

To set up this project locally, make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Setup Instructions

Follow the steps below to set up and run the project on your local machine.

### 1. Clone the Repository

### 2. Create a .env File

You will need to create a .env file to configure environment variables for local development. A sample .env.example file is provided in the repository.

```
cp .env.example .env
```

Edit the .env file to update the values as needed:

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

Pull the necessary Docker images for FastAPI and PostgreSQL.
Build the FastAPI application image.
Run the application on http://localhost:8000.
Expose PostgreSQL on port 5432 for database interactions.

### 4. Running the Service

Once the services are running, you can access the FastAPI application via:

http://localhost:8000

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
