# FastAPI CRUD Project

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

1. Pull the Docker image
```
docker pull mateoscarlos/fastapi_crud
```  

You can also clone de repository following these steps: 

1. Clone the repository:
```
git clone https://gitlab.com/mateoscarlos/fastapi_crud.git
```

2. Change to the project directory:
```
cd fastapi_crud
```

3. Build the Docker image:
```
docker build -t <image_name> .
```
4. Run the Docker container:
```
docker run -d -p <host_port>:8000 --name <container_name> <image_name>
```

The application should now be running on `http://localhost:8000`.


## Contributing

If you'd like to contribute to this project, feel free to open a pull request or raise an issue.
