# Docker Deployer App

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
```
docker_deployer/
│
├── app/                     # Main application logic
│   ├── main.py              # Application entry point
│   └── api/                 # API endpoints for deployment and container operations
│       ├── container_ops.py
│       └── deploy.py
│
├── utils/                   # Utility modules
│   └── docker_client.py     # Docker client abstraction
│
├── services/                # Likely for internal service logic (to check further)
│
├── models/                  # Data models (probably Pydantic or DB models)
│
├── tests/                   # Unit tests
│
├── requirements.txt         # Dependencies
└── venv/                    # Virtual environment (can be ignored)

```


---

##  Setup & Installation

### 1. Clone the Repository

```bash
git clone git@github.com:your-username/docker_deployer.git
cd docker_deployer
```

### 2. Create and Activate a Virtual Environment 

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Ensure Docker is Installed and Running

```bash
Installed → Get Docker
Running (use docker ps to verify)
```

### 5. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```



