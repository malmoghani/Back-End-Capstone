===========================================================
LITTLE LEMON API - PEER REVIEW TESTING GUIDE
===========================================================

Project Overview:
This API allows for menu management and table bookings 
for the Little Lemon restaurant. It uses Django REST 
Framework for API logic and Djoser for authentication.

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
===========================================================