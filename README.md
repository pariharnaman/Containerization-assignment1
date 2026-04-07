# Containerized Web Application with PostgreSQL

A containerized backend application built with **Node.js + Express** and **PostgreSQL**, deployed using **Docker** and **Docker Compose**.

---

## Project Overview

This project demonstrates how to build and deploy a multi-container web application using Docker within a virtualized environment.

## Tech Stack

* Backend API: Python (Flask)
* Database: PostgreSQL
* Containerization: Docker
* Orchestration: Docker Compose
* Virtualization: Multipass
* Networking: Docker IPvlan

## Architecture

The application consists of:

* a backend API developed using Python (Flask)
* a PostgreSQL database running in a separate container
* a Docker Compose configuration to manage and orchestrate both services

To simulate a real-world deployment environment, a virtual machine was created using Multipass. The project files were transferred from the host system to the VM, where all Docker operations were performed.

The backend and database services are connected using a custom Docker IPvlan network, allowing each container to have its own IP address within a defined subnet. This setup enables direct communication between containers, similar to how services interact in a real network environment.

Docker Compose is used to build and run the containers inside the VM, ensuring proper service orchestration. Additionally, Docker volumes are configured to provide persistent storage for the PostgreSQL database, ensuring that data is retained even after containers are stopped or restarted.

## Key Concepts Demonstrated

* Containerization using Docker
* Service orchestration with Docker Compose
* Virtual machine setup using Multipass
* Custom Docker networking with IPvlan
* Data persistence using Docker volumes

This project serves as a practical example of modern backend infrastructure deployment.

---

## Objectives

The main goals of this project are:

- to containerize the backend application
- to run the database in a separate container
- to connect multiple containers using Docker networking
- to persist database data using Docker volumes
- to use Docker Compose for easier orchestration
- to optimize the backend image using a multi-stage build

---
## Screenshot Proofs

### 1) Docker Network Inspect

![](./images/network%20inspect.png)


### 2) Docker Inspect Backend API

![](./images/ip%20address%20expose.png)


### 3) Docker Volume Inspection

![](./images/vol%20persistence.png)



















---






## Technology Stack

### Backend
- Node.js
- Express.js
- PostgreSQL driver (`pg`)

### Database
- PostgreSQL

### DevOps / Containerization
- Docker
- Docker Compose

---

## Project Structure

```text
project
│
├── backend
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
│
├── database
│   └── Dockerfile
│
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md