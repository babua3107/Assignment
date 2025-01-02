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
2. git clone repo url
3. install required package
4. cd Assignment-main  To Main folder
5. cd Assignment-main  To sub folder
6. python manage.py makemigrations  # To create migraton
7. python manage.py migrate #Migrate and create table in DB.
8. Python manage.py createsuperuser
9. python manage.py runserver to run
10. Generate Token Wih Post of username and Password
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
   
