# AppDev-Lab
Final Midterm Project for CC105 LAB

# Task Manager

Task Manager is a Django-based CRUD application designed to help manage tasks with specific business logic.

## Features
- Create, Read, Update, and Delete tasks
- User authentication and authorization
- Task categorization and filtering
- Responsive UI

## Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Django (latest stable version)
- MySQL (using XAMPP for local development)
- Virtualenv (optional but recommended)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/task_manager.git
cd task_manager
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Database Settings
Update the `settings.py` file in the `task_manager` project directory to match your MySQL configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_manager_db',
        'USER': 'root',  # Update if using a different MySQL user
        'PASSWORD': '',  # Set your MySQL password
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Create a Superuser (Optional for Admin Access)
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 7. Run the Development Server
```sh
python manage.py runserver
```

Your application will be available at `http://127.0.0.1:8000/`.


## License
This project is licensed under the MIT License.

