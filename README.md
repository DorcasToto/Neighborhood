# Neigborhood
## Description
This is a website that allows one to join a neigborhood and post things around the hood and also view various businesses in the hood.


### Author
1. Dorcas Cherono
2. Susan Kathoniey
3. Hassan Juma
4. Kennedy Kiptoo
5. Silvia Kago

# Features

A normal authenticated user can be able to:
    a) Sign in to the application to start using it.
    b) Set up a profile which contains:
        - My name 
        - My location 
        - My neighborhood name 
    c) Find a list of different businesses in my neighborhood.
    d) Find Contact Information for the emergency services e.g health department, in his/her 
       neighborhood.
    e) Create Posts that will be visible to everyone in my neighborhood.
    f) Change My neighborhood when I decide to move out.
    g) Users can only belong to one neighborhood at a time.
    h) Only view details of a single neighborhood.

The neighbourhood administrator can be able to:
    i)  Add information about neighborhoods for example: Add businesses, health care centers etc.
    ii) Perform all the operations of a normal user.

The system administrator can be able to:
    - Create neighborhoods
    - Delete neighborhoods 
    - Edit neighborhood information
    - See all users
    - Change user statuses: Either from neighborhood admin to regular user, or the opposite.
    - Remove users.

## Project live site
  This is the live .[ Click for the demo]( https://hood256.herokuapp.com/)

# Technologies Used
- Python.
- Django (Python framework)

# Installation

a. Create and activate virtualenv.
b. Install required packages
pip install -r backend/requirements.txt.
c. Setup
cd backend copy settings.py.txt to settings.py and update the db credentials.(If you are using SQLLite)
d. Setup database
python manage.py migrate
e. Run the server
python manage.py runserver
f. Check if the application is running correctly
g. Create a superuser for the admin backend
python manage.py createsuperuser
h. Login as superuser

# Endpoints
You can access the api end points by visiting the following sites 

- loginendpoint (https://hood256.herokuapp.com/auth/login/)
- view hoods endpoint (https://hood256.herokuapp.com/api/v1/view_hood/%3Cpk%3E/)
- edit profile endpoint (https://hood256.herokuapp.com/api/v1/profile/%3Cpk%3E/ )
- signupendpoint (https://hood256.herokuapp.com/auth/signup/)
- view hoods endpoint (https://hood256.herokuapp.com/api/v1/hoods/)
- create post on a hood endpoint (https://hood256.herokuapp.com/api/v1/post/)
- current user endpoint (https://hood256.herokuapp.com/currentuser/)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/DorcasToto/Neighborhood-Frontend/blob/master/LICENSE)

© [DorcasToto](https://github.com/DorcasToto)

:satisfied: