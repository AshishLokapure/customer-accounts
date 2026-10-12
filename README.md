# Customer Accounts Microservice

[![Build Status](https://github.com/AshishLokapure/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/AshishLokapure/devops-capstone-project/actions/workflows/ci-build.yaml)

## Project Description

The **Customer Accounts Microservice** is a RESTful API application developed as part of the Coursera DevOps Capstone Project. It provides endpoints for managing customer account information and demonstrates software development, automated testing, continuous integration, application security, containerization, and deployment automation.

## Features

- Create a customer account
- Read an individual customer account
- List all customer accounts
- Update an existing customer account
- Delete a customer account
- RESTful API endpoints with JSON responses
- Automated unit tests and code coverage
- Code quality checks using Flake8 and Pylint
- Continuous Integration using GitHub Actions
- Security headers using Flask-Talisman
- Cross-Origin Resource Sharing (CORS) using Flask-CORS
- Docker containerization
- Kubernetes deployment support
- Continuous Delivery automation using Tekton

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | REST API framework |
| Flask-SQLAlchemy | Database integration and ORM |
| SQLite | Default development database |
| PostgreSQL | Supported database option |
| Nose / nosetests | Automated test execution |
| Coverage | Test coverage reporting |
| Flake8 | Code style and linting |
| Pylint | Static code analysis |
| GitHub Actions | Continuous Integration workflow |
| Flask-Talisman | HTTP security headers |
| Flask-CORS | Cross-origin request policies |
| Docker | Application containerization |
| Kubernetes | Container orchestration |
| Tekton | Continuous Delivery pipeline automation |

## REST API Operations

The service supports the following account operations:

| Operation | HTTP Method | Endpoint |
|---|---|---|
| Create an account | POST | `/accounts` |
| List all accounts | GET | `/accounts` |
| Read an account | GET | `/accounts/{account_id}` |
| Update an account | PUT | `/accounts/{account_id}` |
| Delete an account | DELETE | `/accounts/{account_id}` |

The API accepts and returns JSON data where applicable. The account identifier is used to access, update, or delete an individual account.

## Continuous Integration

The GitHub Actions workflow is located at:

`.github/workflows/ci-build.yaml`

The workflow is configured to:

1. Check out the repository source code.
2. Set up the Python environment.
3. Install application and testing dependencies.
4. Run Flake8 linting.
5. Run Pylint static analysis.
6. Execute unit tests using `nosetests`.
7. Generate and report test coverage.

The build-status badge at the top of this README links to the actual GitHub Actions workflow for this repository. Its displayed status updates when the workflow runs.

## Application Security

The application uses Flask-Talisman to configure HTTP security headers and Flask-CORS to manage cross-origin requests. Automated tests cover account operations, security headers, and CORS behavior.

Security settings should be configured appropriately for the deployment environment, especially when HTTPS and reverse proxies are involved.

## Docker Containerization

The Dockerfile defines the environment used to package the Customer Accounts Microservice into a container image. It uses Python, installs the application dependencies, copies the application source code, and exposes port 8080.

## Kubernetes Deployment

The application is designed to support deployment to Kubernetes. A deployment can manage application pods and ReplicaSets, while a Kubernetes Service provides network access to the application.

## Continuous Delivery

The project includes Continuous Delivery as a deployment objective, using Tekton pipeline automation to build and deploy the application to Kubernetes when the corresponding pipeline configuration is available and successfully executed.

## Project Structure

```text
devops-capstone-project/
├── .github/
│   └── workflows/
│       └── ci-build.yaml
├── service/
│   ├── common/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_accounts.py
├── Dockerfile
├── requirements.txt
├── setup.cfg
├── user-story.md
├── README.md
└── LICENSE
```

## Project Objective

The objective of this project is to apply DevOps practices throughout the application lifecycle, including source control, automated quality checks, unit testing, security configuration, containerization, and deployment automation.

## Author

Developed as an educational project for the Coursera DevOps Capstone Project.

## License

This project is intended for educational purposes. Refer to the repository's LICENSE file for licensing details.
