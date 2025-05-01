# Deployer App

A Python-based application for managing deployments and container operations using Docker. It provides an API interface to handle deployment processes, container lifecycle operations, and abstracts Docker logic for easier integration and testing.

---

## 🚀 Features

- API endpoints for deploying services and managing Docker containers
- Modular structure with separation of concerns
- Easy to extend and maintain
- Docker client abstraction for safe and reusable operations
- Unit tests to ensure code reliability

---

## 🗂️ Project Structure

deployer_app/ ├── app/ │ ├── main.py # FastAPI application entry point │ └── api/ │ ├── container_ops.py # Container management endpoints │ └── deploy.py # Deployment-related logic ├── utils/ │ └── docker_client.py # Docker SDK wrapper ├── services/ # Internal service logic (TBD) ├── models/ # Pydantic/DB models ├── tests/ # Unit tests ├── requirements.txt # Dependencies └── venv/ # Virtual environment (excluded from Git)


---

## 🚀 Features

- 🔌 **FAST API** to manage Docker containers
- 🐳 Start, stop, and list containers
- 🔐 SSH-based deployment integration
- ♻️ Modular, maintainable structure using FastAPI and Docker SDK

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone git@github.com:your-username/deployer_app.git
cd deployer_app


