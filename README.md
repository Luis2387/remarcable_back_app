Django Backend - Remarcable Back App

Project Overview

This is the backend API for the Remarcable project, built with Django and Django REST Framework (DRF). It provides product management features, including filtering by categories, tags, and descriptions.


Features:

RESTful API for managing products, categories, and tags.

Search and filtering functionality.

Admin interface for data management.

Automatic superuser creation if not existing.

Deployed on Render.


Installation & Setup:

Prerequisites:

Ensure you have the following installed:

Python 3.x

pip (Python package manager)

Virtual environment (recommended)

PostgreSQL (or SQLite for local testing)


Clone the Repository

git clone https://github.com/Luis2387/remarcable_back_app

3
Create and Activate a Virtual Environment

python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows


Install Dependencies

pip install -r requirements.txt


Set Up Environment Variables

Create a .env file and configure it with:

DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Or PostgreSQL URL


Apply Migrations & Create Superuser

python manage.py migrate
python manage.py createsuperuser  # Optional if env variables are set

Populate the Database (Optional)

python manage.py runscript populate_db


Run the Server

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/api/


API Endpoints


GET

/api/products/

List all products

GET

/api/products/?q=term

Search by description

GET

/api/products/?category=1

Filter by category

GET

/api/products/?tags=1,2

Filter by tags

GET

/api/categories/

List all categories

GET

/api/tags/

List all tags



Deployment (Render)

Push changes to GitHub.

Connect Render to the repository.

Configure environment variables.

Set up Build Command:

pip install -r requirements.txt
python manage.py migrate
python manage.py runscript populate_db  # Optional

Start the service.


Assumptions & Notes

Filtering is done via Django ORM queries.

No pagination implemented due to a small dataset.

If scaling is required, pagination and caching should be added.
