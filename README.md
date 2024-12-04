# Leave Management System

A Django-based leave management system that allows users to create, view, and manage leave requests.

## About the Application

This leave management system streamlines the process of handling employee leave requests in an organization. It provides a hierarchical approval system where:

- Employees can submit leave requests
- Managers can review and approve/reject leave requests from their team members
- HR administrators can oversee all leave requests and manage user roles

## Role-Based Access Control (RBAC)

The system implements three main user roles:

1. **Employee**
   - Can create new leave requests
   - View their own leave history
   - View their leave balance

2. **Manager**
   - Inherits all Employee permissions
   - Can view leave requests from their team members
   - Approve or reject leave requests


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

## Environment Variables

Create a `.env` file in the root directory with the following PostgreSQL database configuration:

```plaintext
PGDATABASE=your_database_name
PGUSER=your_database_user
PGPASSWORD=your_database_password
PGHOST=your_database_host
PGPORT=5432
```

Required environment variables:
- `PGDATABASE`: PostgreSQL database name
- `PGUSER`: PostgreSQL username
- `PGPASSWORD`: PostgreSQL password
- `PGHOST`: Database host address
- `PGPORT`: Database port number (default: 5432)

Note: If no environment variables are set, the application will default to using SQLite3 as the database.

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
