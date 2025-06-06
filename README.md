# django-multi-role-auth

# Django Multi-Role Authentication System

This is a Django-based web application that allows **signup** and **login** for multiple user types — specifically **Patients** and **Doctors**. Upon successful login, each user is redirected to their respective dashboard displaying their profile details.

---

## 🔧 Features

* Role-based signup and login system
* Two types of users: **Patient** and **Doctor**
* Custom user model with additional fields
* Form validation including password confirmation check
* Dashboard pages for both user roles
* Profile picture upload
* Address fields included in signup
* Clean and modular Django structure

---

## 📸 Demo Video

> 📽️ *Submit a short screen-recorded video showing:*
>
> * Signup as Patient and Doctor
> * Login functionality
> * Redirect to respective dashboard
> * Form validations in action

---

## 🧑‍💻 User Types

* **Patient**
* **Doctor**

Each user type has their own signup process and dashboard display.

---

## 📝 Signup Form Fields

* First Name
* Last Name
* Profile Picture
* Username
* Email
* Password
* Confirm Password
* Address:

  * Line 1
  * City
  * State
  * Pincode

Includes password confirmation check and basic validations.

---

## 🔐 Authentication Flow

1. **Sign Up** as Patient or Doctor
2. Backend checks password match and saves data
3. Redirects to respective **dashboard page**
4. Dashboard displays user's submitted data

---

## 🏗️ Tech Stack

* Python 3.x
* Django 4.x
* SQLite3 (default)
* HTML/CSS (for templates)

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/django-multi-role-auth.git
cd django-multi-role-auth

# Create virtual environment and activate
python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run development server
python manage.py runserver
```

---

## 📂 Project Structure Overview

```
django-multi-role-auth/
│
├── core/                 # Main Django app
│   ├── models.py         # Custom User Model and Profiles
│   ├── forms.py          # Signup forms for each role
│   ├── views.py          # Signup, login, dashboard logic
│   ├── urls.py           # App URL patterns
│   └── templates/        # HTML templates
│
├── media/                # Uploaded profile pictures
├── static/               # Static files (CSS, JS)
├── manage.py
└── db.sqlite3
```






