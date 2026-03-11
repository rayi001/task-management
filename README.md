# Task Manager Backend

A Django REST API backend for task management application.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd task-manager-backend
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment (Windows)
   venv\Scripts\activate
   
   # Activate virtual environment (Linux/Mac)
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## Project Structure

```
task-manager-backend/
├── venv/                    # Virtual environment
├── task_manager/            # Django project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── tasks/                   # Django app for task management
│   ├── __init__.py
│   ├── admin.py            # Admin interface
│   ├── apps.py             # App configuration
│   ├── migrations/         # Database migrations
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   └── views.py            # API views
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## API Endpoints

Once the app is developed, the API will include:

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Get a specific task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task

## Development

### Adding New Dependencies

1. Install the package:
   ```bash
   pip install package-name
   ```

2. Update requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

### Running Tests

```bash
python manage.py test
```

### Creating New Apps

```bash
python manage.py startapp app_name
```

Don't forget to add the new app to `INSTALLED_APPS` in `task_manager/settings.py`.
