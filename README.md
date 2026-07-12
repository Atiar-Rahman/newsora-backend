# newsora-backend

### CustomUser Setup
### authentication uses externall package
 - dj_rest_auth
 - all_auth
 - simple_jwt_authentication


 ### New Usesr Register and Login and set user profile
 

---

### 🔗 Authentication Setup Reference

This project uses **dj-rest-auth** for authentication.

📘 Official Documentation:
[https://dj-rest-auth.readthedocs.io/en/latest/getting-started/installation/](https://dj-rest-auth.readthedocs.io/en/latest/getting-started/installation/)

---

#### 📦 Quick Setup Summary

For full installation and configuration guide, follow the official docs above.

---

#### 🧩 Base Features Used

* Registration with email verification
* JWT authentication
* Password reset
* User management API

---

### 💡 Alternative (clean clickable style for GitHub README)

If you want better README style:

```markdown
#### 🔗 Official Docs

- https://dj-rest-auth.readthedocs.io/en/latest/getting-started/installation/
```

---

### 🚀 Best Practice (Pro README style)

```markdown
> 📘 Full documentation: https://dj-rest-auth.readthedocs.io/en/latest/getting-started/installation/
```

---

### ✔️ Recommendation

For GitHub/portfolio project:

👉 use this:

```markdown
📘 Official Documentation: https://dj-rest-auth.readthedocs.io/en/latest/getting-started/installation/
```

---

## Authenthentication complete used doc
[dj_rest_auth](https://dj-rest-auth.readthedocs.io/en/latest/)
[allauth](https://docs.allauth.org/en/latest/)

----
# project setup and locally run


# Blog Backend API

A RESTful Blog Backend API built with Django, Django REST Framework, and PostgreSQL.

---

## 🚀 Features

- User Authentication
- Role Based Permission
- Blog CRUD Operations
- Category Management
- Tag Management
- Comment & Reply System
- Like System
- Bookmark System
- Blog View Tracking
- Soft Delete & Restore
- Admin Management
- API Documentation

---

# 🛠️ Tech Stack

- Python 3.12+
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Supabase PostgreSQL (Production)
- Pillow (Image Processing)

---

# 📁 Project Structure

```

blogs-backend/

│
├── blogs/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── comments/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
├── manage.py
└── README.md

````

---

# ⚙️ Local Setup Guide

## 1. Clone Repository

```bash
git clone <repository-url>

cd blogs-backend
````

---

# 2. Create Virtual Environment

Linux / Mac:

```bash
python3 -m venv env
```

Windows:

```bash
python -m venv env
```

---

# 3. Activate Virtual Environment

Linux / Mac:

```bash
source env/bin/activate
```

Windows:

```bash
env\Scripts\activate
```

---

# 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 5. Environment Variables Setup

Create `.env` file in project root:

```
SECRET_KEY=your_secret_key

DEBUG=True


DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=localhost
DB_PORT=5432


JWT_SECRET_KEY=your_jwt_secret
```

---

# 6. Database Setup

## PostgreSQL

Create database:

```sql
CREATE DATABASE blog_db;
```

Update database settings:

```python
DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.postgresql",

        "NAME": env("DB_NAME"),

        "USER": env("DB_USER"),

        "PASSWORD": env("DB_PASSWORD"),

        "HOST": env("DB_HOST"),

        "PORT": env("DB_PORT"),

    }
}
```

---

# 7. Run Migration

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

# 8. Create Super User

```bash
python manage.py createsuperuser
```

Example:

```
username:
email:
password:
```

---

# 9. Run Development Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

This project uses JWT Authentication.

Login:

```
POST /api/auth/login/
```

Example:

```json
{
    "email":"admin@gmail.com",
    "password":"password"
}
```

Response:

```json
{
    "access":"jwt_access_token",
    "refresh":"jwt_refresh_token"
}
```

Use token:

```
Authorization: Bearer <access_token>
```

---

# 📚 API Endpoints

## Users

| Method | Endpoint             | Description   |
| ------ | -------------------- | ------------- |
| POST   | /api/users/register/ | Register user |
| POST   | /api/auth/login/     | Login         |
| GET    | /api/users/          | User list     |

---

## Blog

| Method | Endpoint         | Description  |
| ------ | ---------------- | ------------ |
| GET    | /api/blogs/      | Blog list    |
| GET    | /api/blogs/{id}/ | Blog details |
| POST   | /api/blogs/      | Create blog  |
| PUT    | /api/blogs/{id}/ | Update blog  |
| DELETE | /api/blogs/{id}/ | Soft delete  |

---

## Category

| Method | Endpoint                           |
| ------ | ---------------------------------- |
| GET    | /api/blog-categories/              |
| POST   | /api/blog-categories/              |
| DELETE | /api/blog-categories/{id}/         |
| POST   | /api/blog-categories/{id}/restore/ |

---

## Comment

| Method | Endpoint            |
| ------ | ------------------- |
| GET    | /api/comments/      |
| POST   | /api/comments/      |
| DELETE | /api/comments/{id}/ |

---

# 🧹 Soft Delete System

Deleted objects are not removed permanently.

Example:

```python
blog.soft_delete()
```

Restore:

```python
blog.restore()
```

Hard delete:

```python
blog.hard_delete()
```

---

# 🧪 Testing

Run tests:

```bash
python manage.py test
```

---

# 📖 API Documentation

Swagger:

```
/swagger/
```

Redoc:

```
/redoc/
```

---

# 🐳 Docker Setup (Optional)

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

---

# Deployment

Production environment:

* Set DEBUG=False
* Configure allowed hosts
* Use PostgreSQL
* Configure static/media storage
* Setup environment variables

---

# 👨‍💻 Developer

Your Name

GitHub:
[https://github.com/yourusername](https://github.com/yourusername)

---

# License

MIT License






