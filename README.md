# Leave Management System

A Django-based leave management system that allows users to create, view, and manage leave requests.

## Features

- User authentication (login/logout)
- Create leave requests with start date, end date, and reason
- View list of leave requests
- Status tracking for leave requests (pending/accepted/rejected)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Leave-Management.git
cd Leave-Management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

## Running Tests

The project includes comprehensive unit tests for all view methods. To run the tests:

```bash
python manage.py test leave_requests.tests
```

The test suite includes:
- Authentication tests (login/logout)
- Leave request creation tests
- View access permission tests
- Form validation tests

## Running the Development Server

To start the development server:

```bash
python manage.py runserver
```

The application will be available at http://localhost:8000/

## Project Structure

- `leave_requests/`: Main application directory
  - `views.py`: Contains all view logic
  - `models.py`: Database models
  - `forms.py`: Form definitions
  - `tests.py`: Unit tests
  - `templates/`: HTML templates
- `leaf/`: Project configuration directory
  - `settings.py`: Django settings
  - `urls.py`: URL configuration
