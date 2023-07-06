# Magnify

**Django CRUD Operations and REST APIs**
This project demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations using Django and the creation of REST APIs with authentication.

**Installation**
Clone the repository:
git clone <repository_url>
A.Install the required dependencies:
pip install -r requirements.txt
B.Set up the Django project:
python manage.py migrate

**USAGE**
Start the development server:
python manage.py runserver
The API endpoints will be accessible at http://localhost:8000/books/.


**API Endpoints:**

    GET /books/: Get a list of all books.
    POST /books/: Create a new book.
    GET /books/{id}/: Get details of a specific book.
    PUT /books/{id}/: Update a specific book.
    DELETE /books/{id}/: Delete a specific book.


**Authentication**

The API endpoints require authentication. You can obtain an authentication token by sending a POST request
