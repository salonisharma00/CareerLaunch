# 🚀 CareerLaunch — Placement Preparation System

CareerLaunch is a full-stack web application designed to help students prepare for campus placements through a single, structured platform.

It brings together aptitude practice, coding challenges, technical preparation, company-specific preparation, and personalized progress tracking in one place.

## 🌐 Live Demo

**Live Website:**  
https://careerlaunch-ia07.onrender.com/

## 📌 Project Overview

Preparing for placements often requires students to use multiple platforms for aptitude, coding, technical topics, and company research.

CareerLaunch solves this problem by providing a centralized placement preparation system where students can:

- Practice aptitude questions
- Solve coding challenges
- Prepare technical interview questions
- Explore company-specific information
- Track preparation progress
- Review test performance
- Monitor coding activity and accuracy

## ✨ Features

### 🧠 Aptitude Preparation
- Quantitative aptitude
- Logical reasoning
- Verbal reasoning
- Practice questions
- Test results and performance tracking

### 💻 Coding Preparation
- Coding challenge collection
- Individual coding problem pages
- Answer submission
- Attempt tracking
- Coding accuracy statistics

### 🎯 Technical Preparation
- Technical interview questions
- Topic-based filtering
- Show/hide answers
- Preparation-focused interface

### 🏢 Company Preparation
- Company profiles
- Eligibility information
- Required skills
- Interview rounds
- Preparation tips

### 📊 Personalized Dashboard
- Overall preparation progress
- Tests completed
- Problems solved
- Companies prepared
- Best and average scores
- Category-wise performance
- Strongest and weakest areas
- Coding activity
- Personalized recommendations
- Recent activity

### 🔐 Authentication
- User registration
- User login
- User logout
- Protected dashboard
- Personalized user experience

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend
- Python
- Django

### Database
- SQLite

### Deployment
- GitHub
- Render
- Gunicorn
- WhiteNoise

## 🏗️ Project Structure

```text
CareerLaunch/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── placement/
│   ├── migrations/
│   ├── templates/
│   │   └── placement/
│   ├── static/
│   │   └── placement/
│   │       └── css/
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── placement_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── venv/