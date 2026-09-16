# DevSecOps AWS Deployment Pipeline

[![DevSecOps Build and Push to AWS ECR](https://github.com)](https://github.com)

An automated CI/CD pipeline featuring static application security testing (SAST), containerized build systems, and fully automated deployment structures to AWS cloud infrastructure.

## 🏗️ System Architecture & DevSecOps Flow

This repository implements a fully automated, hardened CI/CD pipeline built around shift-left security principles:

1. **Static Analysis (SAST):** Integrated **Semgrep** directly into the GitHub Actions runner to scan for high-risk vulnerabilities (Hardcoded Secrets and SQL Injection vectors) before any infrastructure compilation occurs.
2. **Containerization & Registry Management:** Built optimized **Docker** images on the runner, tagging and securely pushing artifacts to **AWS Elastic Container Registry (ECR)** using temporary IAM runner credentials.
3. **Automated Continuous Deployment (CD):** Leveraged programmatic SSH handling via automated workflows to connect to an **AWS EC2** instance, safely managing background processes to dynamically pull the latest image layers from ECR.
4. **Runtime Security Hardening:** Implemented strict container port isolation mapping (external Port 80 to internal flask runtime Port 5000), backed by automated SQLite operational state triggers to prevent 500 runtime crashes.

