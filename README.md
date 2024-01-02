# Online_Judge

Welcome to the Online Judge, a powerful platform designed to evaluate and assess programming skills through a systematic and automated process. This application serves as a hub for coding challenges, algorithmic problem-solving, and competitive programming exercises.

## Introduction

This document provides instructions for setting up and running the project locally.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python
- Git
- Docker

## Getting Started

Follow these steps to set up the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/dee077/Online_Judge.git
   cd my-django-project
   ```

2. **Create and Activate Virtual Environment:**

    Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    MacOs:  
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  
    ```

3. **Install Dependencies:**
    
    ```bash
    pip install -r requirements.txt
    ```

5. **Database Migration:**
    
    ```bash
    python manage.py migrate
    ```

6. **Run the Application**

    ```bash
    python manage.py runverver
    ```
    This command starts the application and its dependencies
    The application should now be running at http://localhost:8000/. You can access the Django admin panel at    
    http://localhost:8000/admin/

7. **Super User Creadnetials**
    
    Username: 
        ```
        admin
        ```
    Password: 
        ```
        Deepanshu27@
        ```