# Neigborhood
## Description
This is a website that allows one to join a neigborhood and post things around the hood and also view various businesses in the hood.


### Author
1. Dorcas Cherono
2. Susan Kathoniey
3. Hassan Juma
4. Kennedy Kiptoo
5. Silvia Kago

## Front-End link

Click the [ link ] (https://github.com/DorcasToto/Neighborhood-Frontend) to view the front-end repository

# Features

A normal authenticated user can be able to:
  - Sign in to the application to start using it.
  - Set up a profile which contains:
          1. My name 
          2. My location 
          3. My neighborhood name 
  - Find a list of different businesses in my neighborhood.
  - Find Contact Information for the emergency services e.g health department, in his/her 
        neighborhood.
  - Create Posts that will be visible to everyone in my neighborhood.
  - Change My neighborhood when I decide to move out.
  - Users can only belong to one neighborhood at a time.
  - Only view details of a single neighborhood.

The neighbourhood administrator can be able to:
  - Add information about neighborhoods for example: Add businesses, health care centers etc.
  - Perform all the operations of a normal user.

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

- Create and activate virtualenv.
- Install required packages: 
pip install -r backend/requirements.txt.

# Setup

- copy settings.py.txt to settings.py and update the db credentials.(If you are using SQLLite)
- Setup database
- run python manage.py migrate
- Run the server
- Check if the application is running correctly
- Create a superuser for the admin backend
- run python manage.py createsuperuser and input the credentials
- Login as superuser

# Endpoints
Download [ postman]( https://www.postman.com/downloads/ ) to access the following endpoints

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