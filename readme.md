# Fleet Management System

A Django-based fleet management system for tracking vehicles and stations.

## Prerequisites

- Python 3.11 or higher
- Git
- pip (Python package installer)

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd fleet_project
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
   - Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - Linux/MacOS:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Apply database migrations
```bash
python manage.py migrate
```

6. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin credentials.

## Running the Application

1. Start the development server
```bash
python manage.py runserver
```

2. Access the application:
   - Main site: http://127.0.0.1:8000
   - Admin interface: http://127.0.0.1:8000/admin
   - Fleet Map: http://127.0.0.1:8000/map


## Project Structure

```
fleet_project/
├── fleet/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── admin.py          # Admin interface configuration
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   └── urls.py           # URL routing
├── fleet_project/         # Project settings
├── manage.py             # Django command-line utility
└── requirements.txt      # Project dependencies
```
