# 🍋 Little Lemon Restaurant API

This is the Back-End Capstone project for the Meta Back-End Developer professional certificate. It features a fully functional API for menu management and table bookings, secured with professional-grade authentication.
This API allows for menu management and table bookings 
for the Little Lemon restaurant. It uses Django REST 
Framework for API logic and Djoser for authentication.

## 🛠️ Project Features

* **Menu API**: Full CRUD capabilities for restaurant dishes.
* **Booking System**: Secure table reservation management.
* **Authentication**: User registration and token-based login via **Djoser**.
* **Testing**: Automated unit tests for models and views.

---

## 🚀 Getting Started

### 1. Installation

Ensure you have your environment set up on your MacBook:

```bash
# Install dependencies using Pipenv
pipenv install

# Enter the virtual environment
pipenv shell

```

### 2. Database Setup

Ensure your MySQL server is running and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate

```

### 3. Create a Superuser

You will need an admin account to test secured endpoints:

```bash
python manage.py createsuperuser

```

---

## 📡 API Endpoints Map

### 🔓 Public Endpoints

These can be accessed without a token.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/restaurant/` | GET | Home/Index page |
| `/restaurant/menu/` | GET | View all menu items |
| `/auth/users/` | POST | Register a new account |
| `/auth/token/login/` | POST | Obtain Auth Token |

### 🔒 Protected Endpoints

These require the header: `Authorization: Token <your_token>`

| Endpoint | Method | Description |
| --- | --- | --- |
| `/restaurant/menu/` | POST | Add a new menu item (Admin only) |
| `/restaurant/menu/<id>` | GET/PUT/DELETE | Manage specific menu items |
| `/restaurant/booking/tables/` | GET/POST | View and manage table bookings |

---

### 🔓  Endpoints

-----------------------------------------------------------
1. AUTHENTICATION ENDPOINTS (Djoser & DRF)
-----------------------------------------------------------
These endpoints handle user registration and token generation.

* User Registration:
  POST http://127.0.0.1:8000/auth/users/
  
* Token Login (Get your Token):
  POST http://127.0.0.1:8000/auth/token/login/
  
* DRF Default Token Auth:
  POST http://127.0.0.1:8000/restaurant/api-token-auth/

-----------------------------------------------------------
2. MENU ENDPOINTS
-----------------------------------------------------------
* List All Menu Items & Create Item:
  GET/POST http://127.0.0.1:8000/restaurant/menu/

* Single Menu Item (View, Update, Delete):
  GET/PUT/DELETE http://127.0.0.1:8000/restaurant/menu/<id>

-----------------------------------------------------------
3. BOOKING ENDPOINTS (Requires Authentication)
-----------------------------------------------------------
Note: You must include 'Authorization: Token <your_token>' 
in the header to access these.

* List & Manage Table Bookings:
  GET/POST http://127.0.0.1:8000/restaurant/booking/tables/

-----------------------------------------------------------
4. GENERAL PAGES
-----------------------------------------------------------
* Static Home Page:
  http://127.0.0.1:8000/restaurant/

* Django Admin Panel:
  http://127.0.0.1:8000/admin/

## 🧪 Running Tests

To verify the application logic and security:

```bash
python manage.py test tests

```

*Current test suite includes: `test_models.py` and `test_views.py`.*

---

## 🛠️ Tools Used

* **Framework**: Django & Django REST Framework
* **Auth**: Djoser (Token-based)
* **Database**: MySQL
* **Testing**: Django TestCase & APIClient

---

### 💡 Tips for Reviewers

1. Use **Insomnia** or **Postman** for testing.
2. First, POST your credentials to `/auth/token/login/` to get your token.
3. Add the token to the **Auth** tab (Bearer/Token) before trying to access `/restaurant/booking/tables/`.

