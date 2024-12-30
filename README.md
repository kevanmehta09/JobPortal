# Job Portal Application - Django

A simple job portal application built using Django. It allows users to sign up, log in, register their company details, and manage job postings. The application supports creating, editing, and deleting job posts, and ensures that users can only manage job posts associated with their registered company.

## Features
- **User Authentication**: 
  - User sign-up and login functionality.
  - Use Django’s built-in authentication system for user management.
  
- **Company Registration**:
  - Users can register their company details (e.g., Company Name, Address, Contact Number).
  - Each user can register only one company.
  
- **Job Post Management**:
  - Users can create, edit, and delete job posts associated with their registered company.
  - Job details include title, description, location, salary range, and tags.

- **Permissions**:
  - Only authenticated users can access the company registration and job posting features.
  - Users can only manage job posts for their own company.

---

## Project Setup

### 1. **Prerequisites**

Before setting up the project, ensure you have the following installed on your local machine:

- Python 3.x
- Django 4.x

You can install Django using pip:

```bash
pip install django
```


### 2. **Cloning the Repository**
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/kevanmehta09/JobPortal/
cd jobportal
```

### 3. Setting Up the Project
#### Create a Virtual Environment (Optional but Recommended)
It's best practice to create a virtual environment for your Django project to manage dependencies. Run the following command:

```bash
python -m venv venv
```
Activate the virtual environment:

- On macOS/Linux:

```bash
source venv/bin/activate
```
- On Windows:

```bash
.\venv\Scripts\activate
```
### 4. Database Setup
The project uses SQLite as the default database. To set up the database, run the following command:

```bash
python manage.py migrate
```
This will create the necessary database tables for the application.

### 5. Running the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/.

# Application Structure
### 1. Authentication
- Sign Up: Users can register a new account using Django’s built-in UserCreationForm.
- Login: Users can log in using their credentials (username and password).
- Logout: Users can log out of the application.

### 2. Company Registration
Once logged in, users can register their company by providing the following details:

- Company Name
- Address
- Contact Number

A user can only register one company.

### 3. Job Post Management
After registering a company, users can perform the following actions on job posts:

- **Create a Job Post**: Users can add job posts with details like job title, description, location, salary range, and tags.
- **Edit a Job Post**: Users can edit job posts they have created.
- **Delete a Job Post**: Users can delete job posts they have created.
- **View Job Posts**: Users can view a list of all job posts associated with their company.

# URL Patterns

The following URL patterns are defined for the application:

- /: User sign-up page
- /login/: User login page
- /logout/: User logout page
- /companyregister/: Company registration page (requires login)
- /createjob/: Create a new job post (requires login and company registration)
- /updatejob/<int:jobid>/: Edit a job post (requires login and ownership of the post)
- /deletejob/<int:jobid>/: Delete a job post (requires login and ownership of the post)
- /home/: List all job posts and home screen
