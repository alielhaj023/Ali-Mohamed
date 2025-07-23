# 📜 Django JWT Authentication Template

This repository provides a boilerplate template for setting up **JWT authentication** in a **Django** project using the **Django REST Framework (DRF)**. It's a starting point for building secure, token-based authentication systems for Django REST APIs.

## 🚀 Features

- **JWT Authentication**: Implements secure JSON Web Token-based authentication.
- **Django REST Framework**: Provides a robust API setup.
- **User Registration & Login**: Supports authentication using email & password.
- **Token Refresh**: Includes token refresh mechanism.
- **Swagger API Documentation**: Auto-generated API docs for easy testing.
- **Code Quality Tools**: Pre-configured **Pylint, Black, and Pre-commit hooks** for maintaining clean code.
- **Type Checking & Import Sorting (optional)**: Uses **Mypy** and **Isort** for enhanced development.


## 🛠 Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Django 4.x or higher
- Django REST Framework
- PostgreSQL or SQLite (for database)
- Virtual environment (recommended)

## ⚡ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/madhvi-in/django-jwt-auth-template.git
    cd django-jwt-auth-template
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the API at `http://127.0.0.1:8000/api/v1/auth/`.

8. Set Up Google OAuth Credentials
    1. Go to the Google Cloud Console → Create a new project.
    2 .Navigate to APIs & Services → Credentials.
    3. Click Create Credentials → OAuth 2.0 Client ID.
    4. Set Authorized redirect URIs:
        - http://127.0.0.1:8000/accounts/google/login/callback/
    5. Save the Client ID and Client Secret.


## 🔥 API Endpoints

- **POST `/api/v1/auth/register/`**: Register a new user.
- **POST `/api/v1/auth/login/`**: Login with your credentials to get a JWT token.
- **POST `/api/v1/auth/token/refresh/`**: Refresh the JWT token.
- **GET `api/docs`**:


## 🎯 Running Pre-commit Hooks

This template comes with pre-configured **pre-commit hooks** to ensure code quality:

1. Install pre-commit:
    ```bash
    pip install pre-commit
    ```

2. Set up the hooks:
    ```bash
    pre-commit install && pre-commit install-hooks
    ```

3. Run hooks manually for all files:
    ```bash
    pre-commit run --all-files
    ```
The hooks will now **automatically run** before every commit.


### Build and run Docker using Environment variables
You can pass the environment variables when building the Docker image:

```bash
    docker build --env-file .env -t django-jwt-auth-template .
```

Then, when running the container, pass the environment variables to the container:
```bash
    docker run -d -p 8000:8000 --env-file .env --name django-auth django-jwt-auth-template
```


<br>
<hr>

### 🎉 Happy coding! 🚀
