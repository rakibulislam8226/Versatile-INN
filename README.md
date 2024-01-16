# Versatile INN - Restaurant Management Microservice

## Overview

Versatile INN is a microservice-based restaurant management system. It simplifies the management of a parent restaurant, "Versatile INN", and its child restaurants. The system allows for the creation and management of child restaurants and tables, complete with an approval process for new tables.

## Features

- **Manage Child Restaurants:** Owners and co-owners can create and oversee child restaurants.
- **Table Management:** Enables managers of child restaurants to add new tables, which initially have a 'pending' status.
- **Approval Workflow:** Newly added tables require approval from Versatile INN's upper management to change their status to 'active'.

## Technology Stack

- **Python:** Core programming language.
- **Flask:** Web framework for APIs.
- **gRPC:** Communication protocol for microservices.
- **Docker:** Containerization and deployment.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10
- Docker and Docker Compose
- Git

### Installation

1. **Clone the Repository**


### Project structure
```
.
├── commands.txt
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── src
    ├── apps
    │   ├── __init__.py
    │   └── main.py
    ├── grpc_services
    │   ├── __init__.py
    │   ├── restaurant_service_pb2_grpc.py
    │   ├── restaurant_service_pb2.py
    │   ├── restaurant_service.proto
    │   └── restaurant_service.py
    ├── proto
    └── tests
        └── __init__.py
```