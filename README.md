# Weekly Task Manager

Week 3 task for Super 100 Training Classes

## ✨ Features

* **Daily Task Management:** Organize tasks specifically for each day of the week.
* **Add Tasks:** Easily add new tasks to any given day.
* **Mark as Done:** Toggle tasks as complete or incomplete.
* **Delete Tasks:** Remove tasks that are no longer relevant.
* **Intuitive Interface:** A clean and user-friendly design built with Bootstrap 5.
* **Sunday First:** Week starts with Sunday for better weekly planning overview.

## 🚀 Technologies Used

* **Python 3.13.3**
* **Django 5.2.1**
* **SQLite3** (for local development database)
* **Bootstrap 5** (for responsive styling)
* **Google Fonts (Inter)**

## 🖥️ Local Development Setup

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.13.3** (or a compatible version, e.g., 3.9+)
* **pip** (Python package installer, usually comes with Python)
* **Git Bash** (or any Git client)

### 2. Clone the Repository

First, clone this repository to your local machine using Git Bash:

```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/django-weekly-task-manager.git](https://github.com/YOUR_GITHUB_USERNAME/django-weekly-task-manager.git)
# Replace 'YOUR_GITHUB_USERNAME' and 'django-weekly-task-manager' with your actual GitHub username and repository name.
```

Navigate into the cloned project directory:
Bash

cd django-weekly-task-manager # Or whatever you named your repo

### 3. Create and Activate Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

On Windows (Git Bash/CMD/PowerShell):
```bash
python -m venv .venv
source .venv/Scripts/activate
```

On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see (.venv) at the beginning of your terminal prompt, indicating the virtual environment is active.

### 4. Install Dependencies

With your virtual environment active, install the required Python packages:
```bash
pip install Django
```

### 5. Database Setup

Django uses a SQLite database by default for development. You need to apply the database migrations to create the necessary tables.
```bash
python manage.py makemigrations task
python manage.py migrate
```

### 6. Run the Development Server

Finally, start the Django development server:
```bash
python manage.py runserver
```
You should see output similar to:
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 20, 2025 - 16:53:02
Django version 5.2.1, using settings 'week3_task.settings'
Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Quit the server with CONTROL-C.

Open your web browser and navigate to http://127.0.0.1:8000/ to see the application in action.
```

## 🤝 Contributing

Feel free to fork this repository, make improvements, and submit pull requests.

## 📄 License
This project is open-source and available under the MIT License. (You might want to create a https://www.google.com/search?q=LICENSE file in your repo root if you choose this license).

## 📧 Contact
If you have any questions or feedback, feel free to reach out!

venkat374
