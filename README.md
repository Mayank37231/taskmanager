Task Manager API
A simple and secure task management API built with Django and Django REST Framework. This project provides a RESTful interface for users to register, log in, and manage their personal tasks.

🚀 Features
User Authentication: Secure user registration and login using JSON Web Tokens (JWT).

Token-Based Authentication: Access and refresh tokens for secure API access.

CRUD Operations: Full functionality for creating, retrieving, updating, and deleting tasks.

User-Specific Tasks: Users can only manage their own tasks, ensuring data privacy and security.

📦 Technologies Used
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

Django REST Framework: A powerful and flexible toolkit for building Web APIs.

djangorestframework-simplejwt: Provides a simple way to implement JWT authentication.

SQLite3: The default database for Django development.

⚙️ Installation and Setup
Clone the repository:

Bash

git clone https://github.com/Mayank37231/taskmanager.git
cd your-repo-name

Create and activate a virtual environment:

Bash

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install the required dependencies:

Bash

pip install -r requirements.txt

Run database migrations:

Bash

python manage.py makemigrations
python manage.py migrate
Run the development server:

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

🖥️ API Endpoints
Authentication
Endpoint	         Method	    Description		
/api/register/	     POST	    Register a new user.		
/api/login/	         POST	    Authenticate a user and get access/refresh tokens.		
/api/token/refresh/	 POST	    Get a new access token using a refresh token.		


Tasks
Requires an Authorization: Bearer <access_token> header.

Endpoint	            Method	     Description
/api/tasks/	            GET	         Retrieve a list of all authenticated user's tasks.
/api/tasks/	            POST	     Create a new task.
/api/tasks/<int:pk>/	GET	         Retrieve a single task by ID.
/api/tasks/<int:pk>/	PUT	         Fully update a task by ID.
/api/tasks/<int:pk>/	PATCH	     Partially update a task by ID.
/api/tasks/<int:pk>/	DELETE	     Delete a task by ID.