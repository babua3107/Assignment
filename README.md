# Assignment REST API  



## Features  
- Create a new task with a title, description, and status.  
- Retrieve all tasks or fetch a task by its ID.  
- Update the status of a task.  
- Delete a task by its ID.
- JWT-based authentication for API access.

## Requirements  
- Python 3.9 or above  
- Django 4.2.6  
- Django REST Framework 3.14.0
- sqlite3==3.39.4
- djangorestframework-simplejwt for JWT authentication


## Installation  
1. **Clone the Repository:**   
   git clone repo url
   install required package
   cd Assignment-main  To Main folder
   cd Assignment-main  To sub folder
   python manage.py makemigrations  # To create migraton
   python manage.py migrate #Migrate and create table in DB.
   Python manage.py createsuperuser
   python manage.py runserver to run
   Generate Token Wih Post of username and Password
## Test 

- API Endpoints
POST /api/token
Example
{
  "username": "username",
  "password": "testpassword"
}
Access Token Name Copy,
Add this Access token in bearer token everytime for authentication
POST /tasks/ - Create a new task
DATA TO TEST
{
  "title": "Song",
  "description": "Hip-Hop",
  "status": "in-progress"
}

GET /tasks/ - all tasks
GET /tasks/:id/ - task by ID
PUT /tasks/:id/ - Update task status
DELETE /tasks/:id/ - Delete a task by ID
   
