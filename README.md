# FastAPI CRUD Project

**Note:** This project is still under development and not yet complete.

## Overview

This is a FastAPI-based CRUD application using Python, PostgreSQL and Docker. The aim of the project is to provide a simple and efficient way to create, read, update, and delete records.

## Features

- FastAPI for building the API
- PostgreSQL as the database
- Docker for containerization and easy deployment
- Supports Create, Read, Update, and Delete (CRUD) operations

## Getting Started

### Prerequisites

- Docker installed on your machine


### Pull the Docker Container

To run the application you can pull the pre-built Docker container from Docker Hub using the following command:
```
docker pull mateoscarlos/fastapi-crud
```  

You can also clone de repository following these steps: 

1. Clone the repository:
```
git clone https://gitlab.com/mateoscarlos/fastapi_crud.git
```

2. Change to the project directory:
```
cd fastapi-crud
```

3. Build the Docker image:
```
docker build -t fastapi-crud .
```
4. Run the Docker container:
```
docker run -d -p <your_port>:8000 <container_name>
```

The application should now be running on `http://localhost:8000`.


## Contributing

If you'd like to contribute to this project, feel free to open a pull request or raise an issue.
