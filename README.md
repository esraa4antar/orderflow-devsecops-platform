# OrderFlow DevSecOps Platform

A production-like cloud-native DevSecOps project built to demonstrate modern application delivery, infrastructure, security, CI/CD, containerization, and observability practices.

## Project Goal

Build and operate a full-stack application using modern DevOps and DevSecOps practices, progressing from local development to a production-like AWS and Kubernetes environment.

The project is being built incrementally, with each phase focusing on a specific part of the platform lifecycle.

---

## Technology Stack

### Application

* React
* Django REST Framework
* PostgreSQL
* Nginx

### DevOps

* Docker
* Docker Compose
* GitHub Actions
* Terraform
* AWS
* Kubernetes
* Helm
* Argo CD

### DevSecOps

* Trivy
* Kubernetes security best practices

### Observability

* Prometheus
* Grafana
* OpenTelemetry

---

## Project Status

🚧 **Under active development**

### Phase 0 — Project Foundation

* [x] Project repository and structure
* [x] Git and GitHub setup
* [x] SSH authentication with GitHub
* [x] Initial project documentation

### Phase 1 — Backend Foundation

* [x] Django project setup
* [x] Django REST Framework dependencies
* [x] Orders application
* [x] Database migrations
* [x] Django system checks
* [x] Initial automated test

### Phase 2 — CI/CD & Containerization

* [x] Django backend Dockerization
* [x] Production-oriented Gunicorn configuration
* [x] `.dockerignore`
* [x] Docker image build
* [x] Docker image vulnerability scanning with Trivy
* [x] Filesystem vulnerability scanning with Trivy
* [x] GitHub Actions CI pipeline
* [x] Automated Django checks and tests
* [x] PostgreSQL with Docker Compose
* [x] Persistent PostgreSQL volume
* [x] Django ↔ PostgreSQL container networking
* [x] PostgreSQL service container in GitHub Actions
* [x] PostgreSQL health check for CI
* [x] Successful CI run after database integration

### Phase 3 — Infrastructure as Code

* [ ] Terraform setup
* [ ] AWS provider configuration
* [ ] VPC and networking
* [ ] Security groups
* [ ] EC2 infrastructure
* [ ] IAM configuration
* [ ] Terraform variables and outputs

### Phase 4 — Kubernetes

* [ ] Kubernetes cluster setup
* [ ] Application deployments
* [ ] Services
* [ ] ConfigMaps and Secrets
* [ ] Persistent storage

### Phase 5 — Helm

* [ ] Helm chart
* [ ] Configurable environments
* [ ] Helm-based deployment

### Phase 6 — GitOps

* [ ] Argo CD setup
* [ ] GitOps deployment workflow
* [ ] Automated synchronization

### Phase 7 — Monitoring & Observability

* [ ] Prometheus
* [ ] Grafana
* [ ] OpenTelemetry
* [ ] Application and infrastructure metrics

### Phase 8 — Security Hardening

* [ ] Kubernetes security hardening
* [ ] Secrets management improvements
* [ ] Container security improvements
* [ ] Security best-practice review

---

## Phase 2 Architecture

During Phase 2, the application was moved from a local SQLite-based setup to a containerized environment using Docker Compose.

```text
                    Docker Compose
                 ┌──────────────────┐
                 │                  │
                 │  Django Backend  │
                 │   Gunicorn :8000 │
                 │                  │
                 └────────┬─────────┘
                          │
                    Docker Network
                          │
                 ┌────────▼─────────┐
                 │   PostgreSQL     │
                 │      :5432       │
                 └────────┬─────────┘
                          │
                    Persistent Volume
```

---

## CI Pipeline

The current CI pipeline performs:

```text
Git Push / Pull Request
          ↓
   GitHub Actions
          ↓
    Django Checks
          ↓
     Django Tests
          ↓
   Trivy FS Scan
          ↓
    Docker Build
          ↓
  Trivy Image Scan
          ↓
        PASS
```

PostgreSQL is provided as a service container during CI so that Django tests run against PostgreSQL rather than SQLite.

---

## Phase 2 — Key Challenge

One of the issues encountered during CI integration was a database hostname resolution failure.

Locally, Docker Compose allows the Django container to reach PostgreSQL using the service name:

```text
db:5432
```

However, the GitHub Actions runner was initially running Django outside the Docker Compose network, so the `db` hostname could not be resolved.

The solution was to configure PostgreSQL as a GitHub Actions service container and use:

```text
localhost:5432
```

for the CI environment.

This highlighted an important difference between **Docker Compose networking** and the **GitHub Actions runner environment**.

---

## Running Locally

The application can be started using Docker Compose:

```bash
docker compose up -d --build
```

Check running services:

```bash
docker compose ps
```

Run Django migrations:

```bash
docker compose exec backend python manage.py migrate
```

Run Django checks:

```bash
docker compose exec backend python manage.py check
```

---

## Repository Structure

```text
orderflow-devsecops-platform/
├── .github/
│   └── workflows/
├── app/
│   ├── backend/
│   └── frontend/
├── deployment/
│   ├── helm/
│   └── kubernetes/
├── docs/
├── infrastructure/
│   └── terraform/
├── monitoring/
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

> Some directories and components are placeholders for upcoming phases and are not yet fully implemented.

---

## Development Approach

This project is being developed incrementally with a focus on:

* Automation
* Infrastructure as Code
* Security
* Reproducibility
* Containerization
* CI/CD
* Cloud-native architecture
* Observability
* Troubleshooting real-world failures

Each phase is documented as it is implemented, including problems encountered and the solutions applied.

---

## Current Milestone

**Phase 2 — CI/CD & Containerization ✅**

Next:

**Phase 3 — Terraform + AWS ☁️**

