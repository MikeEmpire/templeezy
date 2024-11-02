# Menu Creator

A Django API to create customizable menu templates and generate menu files.

## Installation

1. Clone the repository.
2. Create a virtual environment:
    ```bash
    python3 -m venv menu_env
    source menu_env/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database and run migrations:
    ```bash
    python manage.py migrate
    ```

## Usage
- Start the development server:
    ```bash
    python manage.py runserver
    ```
- Access Swagger API docs at `/swagger/`.

## Dependencies
- Django
- Django REST Framework
- WeasyPrint (for PDF generation)
- PostgreSQL

