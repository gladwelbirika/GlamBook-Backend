# GlamBook - Beauty Appointment Booking System

## Overview

GlamBook is a web-based beauty appointment booking system designed to simplify the process of booking salon services online.

The platform allows clients to browse available beauty services, view prices, choose a stylist, and submit appointment requests. Salon administrators can manage services, stylists, bookings, and payments through the backend system.

The goal of GlamBook is to replace manual booking processes such as phone calls and walk-ins with a simple digital appointment management system.

---

# Features

## Client Features

- Browse available beauty services
- View service descriptions and prices
- View available stylists
- Select preferred services and stylists
- Submit appointment bookings
- Receive booking confirmation

## Admin Features

- Manage service categories
- Add, update, and delete services
- Manage stylists
- View customer bookings
- Update booking status:
  - Pending
  - Confirmed
  - Completed
  - Cancelled
- Manage payments

---

# Technology Stack

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- React Router

## Backend

- Python
- Django
- Django REST Framework
- SQLite Database
- JWT Authentication
- Swagger API Documentation

## DevOps

- Docker
- Docker Compose
- GitHub Actions

---

# System Architecture

```
Client Browser
      |
      |
React Frontend
      |
      |
REST API (Axios)
      |
      |
Django Backend
      |
      |
SQLite Database
```

The frontend communicates with the Django backend through REST API endpoints. The backend handles business logic, database operations, and API responses.

---

# Database Design

GlamBook uses SQLite as the database.

Main database entities:

- Category
- Service
- Stylist
- Booking
- Payment

## Relationships

- A Category can contain many Services
- A Stylist can provide multiple Services
- A Booking belongs to one Service
- A Booking belongs to one Stylist
- A Payment belongs to one Booking

Database diagram:

```
Category
    |
    |
    ↓
Service
    |
    |
    ↓
Booking
    |
    |
    ↓
Payment


Stylist
    |
    |
    ↓
Booking
```

---

# API Documentation

The API is documented using Swagger/OpenAPI.

Available documentation:

```
/api/schema/swagger-ui/
```

Main API endpoints:

## Services

```
GET    /api/services/
POST   /api/services/
PUT    /api/services/{id}/
DELETE /api/services/{id}/
```

## Stylists

```
GET    /api/stylists/
POST   /api/stylists/
PUT    /api/stylists/{id}/
DELETE /api/stylists/{id}/
```

## Bookings

```
GET    /api/bookings/
POST   /api/bookings/
PUT    /api/bookings/{id}/
DELETE /api/bookings/{id}/
```

---

# Installation and Setup

## Backend Setup

Clone the repository:

```bash
git clone <backend-repository-url>
```

Navigate into the backend folder:

```bash
cd GlamBook-Backend
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python3 manage.py migrate
```

Create an admin account:

```bash
python3 manage.py createsuperuser
```

Start the Django server:

```bash
python3 manage.py runserver
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Navigate into the frontend folder:

```bash
cd GlamBook-Frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# Docker Setup

Both frontend and backend are containerized using Docker.

Build and run the application:

```bash
docker compose up --build
```

Application services:

Frontend:

```
http://localhost:3000
```

Backend:

```
http://localhost:8000
```

---

# Docker Services

The Docker Compose configuration contains:

## Backend Container

- Python Django application
- Runs Django REST API
- Port: 8000

## Frontend Container

- React production build
- Served using Nginx
- Port: 3000

---

# Project Structure

```
GlamBook

├── GlamBook-Backend
│
│   ├── booking
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── glambook
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── db.sqlite3
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── manage.py
│
└── GlamBook-Frontend
    │
    ├── src
    │   ├── components
    │   ├── pages
    │   └── api.js
    │
    ├── Dockerfile
    ├── package.json
    └── vite.config.js
```

---

# CI/CD Pipeline

GitHub Actions are configured for continuous integration.

The workflows automatically:

## Backend

- Install Python dependencies
- Run database migrations
- Run Django tests

## Frontend

- Install Node dependencies
- Build React application

Workflows run automatically when changes are pushed or pull requests are created.

---

# Future Improvements

Possible future features:

- User authentication
- Online payments
- Email/SMS booking notifications
- Calendar integration
- Customer reviews
- Salon dashboard analytics

---

# Author

**Gladwel Birika**

