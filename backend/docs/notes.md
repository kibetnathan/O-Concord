This is a simple django project made for Mavuno Young and Fearless and any other churches that might need a data management system. This base version can be tweaked to fit any church structures

[Repository](https://github.com/kibetnathan/Church-Management-System)
## Table of contents

- [About](##about)
- [Technical](##Technical)
- Project timeline
- [To Do List](##To-Do)
- Suggestions

## About

### Features:
##### 1. Role Based Access:
Using role based access members of the church can use the application based on their views with pastors and leaders being able to manage the data of the members
##### 2. Member Groups:
Members are organised into groups such as serving teams, discipleship groups and age groups and have linked data
##### 3. Robust Dashboards
Robust Dashboards for data visualisation and control for every role

##### 4. Messaging Board
A simple messaging board/forum for important communication

### User Roles:
1. Pastors
2. Leaders
3. DG Leaders
4. Members

### Member Groups:
1. Leadership teams
2. Age groups
3. Discipleship Groups
4. Ropes Classes
5. Campus Trend
6. Serving teams

### Collectable Data & Forms:
[Reference Form](https://docs.google.com/forms/d/e/1FAIpQLSeXuBle7_VJ3Gn9nuyRfnZ03McRMGoN37Nxpc_J0BiL5aRXtw/viewform)
The app will have a number of forms for data collection with the following datafields collected:
- Name 
- Age 
- Date Of Birth
- Address/Residence
- Phone number
- Email address
- School/Workplace
- Campus
- DG
- If Serving
- Groups
- Profile photo

The forms/models that will collect data are as follows:
- Profile
- Personal info
- Ministry data

### API Views
- Groups
- Profiles
- 
## Technical

### Technologies used

Some of the tools and technologies used include:

- Django
- Tailwind CSS
- PostgreSQL
- Cloudinary
- Python
- HTML

#### Dependencies:
- django-registration
- cloudinary
- psycopg2
- python-decouple
- django-tailwind
- django_browser_reload
- markdown
- djangorestframework
- django-filter



## Project Timeline

### Week 1
Project Foundations; Django project set up, objectives defined, create custom user authentication and user profiles and a main app, set up cloudinary and define various roles. Create api views and a dashboard for leader roles and a communication channel
Delivered:
- Functional User Profiles and Accounts
- MVP dashboard for leaders
- Simple UI
### Week 2
Core Features; Create Models to handle different kinds of user data, create a robust pastor panel and leadership roles. Create member relationship models and such. Create API endpoints for alternative views.
Delivered:
- Full user hierachies and relationships defined
- Dashboards for all user roles
- Communication channel
## To-Do

- [x] Set Up Repository
- [x] Create README.md
- [x] Set Up Custom Auth Models
- [x] Set Up User Registration
- [x] Create Roles
- [x] Create base template
- [x] Make Home Page
- [x] Set Up Cloudinary
- [x] Define data to be collected
- [x] Define groups
- [x] Create group models
- [x] Create Data models
- [x] Create Robust user registration form
- [ ] Create forms for data submission
- [x] Set Up DRF
- [ ] Create Form for profile update
- [x] Create Serializers
- [x] Create API view for Profile
- [x] Create API views for Groups
- [x] Create API view for Ministry Data
- [ ] Create Auth API
- [ ] Write tests
- [ ] Models for comm channel

## Milestones
- [ ] Full API Views
- [ ] Basic UI
- [ ] Full test suite
- [ ] Dashboards
- [ ] Populate database
- [ ] Member Groups
- [ ] Communication Channel
- [ ] Full UI
- [ ] Deployment