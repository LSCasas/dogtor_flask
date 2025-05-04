# Dogtor

This project allows for the creation and management of pet owners, pets, medical records, and related entities through a secure token-based authentication system. It is structured for scalability and ease of use with environment configurations and ORM integration.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#how-to-use-this-project)
- [Requirements](#requirements)
- [Contribution](#contribution)
- [Learn More](#learn-more)

---

## Project Structure

```
dogtor_flask/
├── README.md
├── requirements.txt
├── dogtor/
│   ├── __init__.py         # App factory and app config
│   ├── config.py           # Environment configuration
│   ├── db.py               # SQLAlchemy instance
│   ├── api/                # Blueprints and routes
│   └── models/             # SQLAlchemy models
└── venv/                   # Virtual environment (not included in repo)
```

---

## Features

- Create and manage pet owners
- Register and edit pet information
- Protected routes use JWT-based authentication
- Schedule veterinary procedures and appointments
- Integrated with Postgres

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LSCasas/dogtor_flask_postgres.git
   cd dogotor_flask_postgres
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   Copy the example file and edit your settings:

   ```bash
   cp example.env .env
   ```

4. **Run the server:**

   ```bash
   python app.py
   ```

---

## How to Use This Project

You can register a new owner by making a POST request to the `/api/owners` endpoint with the following JSON body:

```json
{
  "first_name": "Luis",
  "last_name": "Casas",
  "phone": "555-123-4567",
  "mobile": "555-987-6543",
  "email": "luis@example.com"
}
```

This creates a new record in the `owners` table using

---

## 🔐 Authentication

All protected routes use JWT-based authentication. You must include a valid token in the `Authorization` header:

```
Authorization: Bearer <your_token_here>
```

Token generation and user login are handled in the `/auth` route.

---

## Requirements

- Flask
- python-dotenv
- Flask-SQLAlchemy
- psycopg2
- PyJWT

---

## Contribution

If you want to contribute to this project, follow the steps below:

1. Fork the repository.

2. Create a new branch for your feature:

   ```bash
   git checkout -b feature/new-feature
   ```

3. Make your changes.

4. Commit your changes:

   ```bash
   git commit -am 'Add new feature'
   ```

5. Push your changes to your fork:

   ```bash
   git push origin feature/new-feature
   ```

6. Create a Pull Request for your changes to be reviewed and merged into the main project.

---

## Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [JWT for Python](https://pyjwt.readthedocs.io/)

---

Your feedback and contributions to this project are welcome!
