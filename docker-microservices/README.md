# Docker Microservices — Secure Scaffold

**Author:** Wesley Silva  
**Focus:** Microservices • Docker • DevOps • Cybersecurity

## Overview
This repository shows a production-minded microservices scaffold using Docker Compose.
It includes examples for: an Auth service (FastAPI), an API service (Node/Express),
and a Frontend served by Nginx. Security and operational best practices are applied.

## Features
- Multi-stage Docker builds
- Non-root containers
- Secrets (local file for dev; use vault in prod)
- Healthchecks and resource limits
- Basic reverse proxy (Nginx) with security headers
- CI hints: build, test, image scan (Trivy)

## Quick start (local)
1. Create secrets folder (do not commit):
   ```bash
   mkdir -p secrets
   echo "strong_pg_password_here" > secrets/pg_password.txt
