import os

# Root project name
PROJECT_ROOT = "docker-microservices"

# Directory structure
DIRECTORIES = [
    ".github/workflows",
    "deploy/nginx",
    "docs",
    "secrets",
    "services/auth/app",
    "services/api/src",
    "services/frontend/src",
    "services/frontend/public"
]

# Files with optional default content
FILES = {
    ".gitignore": """# Ignore Python, Node, and Docker build artifacts
__pycache__/
node_modules/
.env
*.pyc
*.log
secrets/
dist/
build/
Dockerfile~
""",

    ".dockerignore": """__pycache__/
node_modules/
.git
.env
*.log
Dockerfile~
secrets/
""",

    "docker-compose.yml": """version: '3.9'
services:
  auth:
    build: ./services/auth
    ports:
      - "8000:8000"
  api:
    build: ./services/api
    ports:
      - "5000:5000"
  frontend:
    build: ./services/frontend
    ports:
      - "3000:80"
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./deploy/nginx:/etc/nginx/conf.d
""",

    "Makefile": """build:
\tdocker-compose build

up:
\tdocker-compose up -d

down:
\tdocker-compose down
""",

    "README.md": """# Docker Microservices — Secure Scaffold

**Author:** Wesley Silva  
**Focus:** Microservices • Docker • DevOps • Cybersecurity

This project demonstrates a secure microservices setup using Docker Compose,
with isolated services for authentication, API gateway, and frontend.
""",

    "LICENSE": """MIT License

Copyright (c) 2025 Wesley Silva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
"""
}

def create_project():
    print(f"🚀 Creating project structure: {PROJECT_ROOT}")
    os.makedirs(PROJECT_ROOT, exist_ok=True)
    os.chdir(PROJECT_ROOT)

    for dir_path in DIRECTORIES:
        os.makedirs(dir_path, exist_ok=True)
        print(f"📂 Created directory: {dir_path}")

    for file_name, content in FILES.items():
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📄 Created file: {file_name}")

    # Create placeholder files in service directories
    placeholders = [
        "services/auth/Dockerfile",
        "services/api/Dockerfile",
        "services/frontend/Dockerfile",
        "deploy/nginx/proxy.conf",
        "docs/architecture.png",
        "docs/presentation.pdf",
        "services/auth/README.md",
        "services/api/README.md",
        "services/frontend/README.md"
    ]
    for path in placeholders:
        with open(path, "w") as f:
            f.write("")
        print(f"🧩 Placeholder: {path}")

    print("\n✅ Project structure created successfully!")

if __name__ == "__main__":
    create_project()
