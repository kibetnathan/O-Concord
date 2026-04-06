This is a simple django project made for Mavuno Young and Fearless and any other churches that might need a data management system. This base version can be tweaked to fit any church structures

[Repository](https://github.com/kibetnathan/Church-Management-System)
## Table of contents

- [About](##about)
- [Technical](##Technical)
- Project timeline
- [To Do List](##To-Do)
- Suggestions

## About
### Target denominations
This tool is aimed at churches with less rigid church structures and few leadership hierarchies.
Our references were:
1. Non Denominational churches
2. Baptist
3. Pentecostal

#### Organisational Structures
 1. Congregationalism
 2. Elder Led
 3. Moses Models

Future versions may include support for higher church and more rigid church structures like Orthodoxy and Catholic churches
More about the organisation structures --> [Church Structures](church_structures.md)
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

### Messaging board:
The messaging board works similarly to a forum page, with posts, and comments.

### Dashboards:
#### 1. Pastor Dashboard
From the pastor dashboard, pastors can view and edit almost all data, similarly to the admin panel and create posts .
**Editable data includes**:
1. Ropes classes:
	- Members
	- Leaders
2. Age groups:
	- Name
	- Desc
	- Pastor
	- Members
3. DGs:
	- Name


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
- django-taggit
- djangorestframework-simplejwt




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
- [x] Create forms for data submission
- [x] Set Up DRF
- [x] Create Form for profile update
- [x] Create Serializers
- [x] Create API view for Profile
- [x] Create API views for Groups
- [x] Create API view for Ministry Data
- [x] Switch To Viewsets
- [x] Update Readme
- [x] Set up JWT
- [x] Create Auth API
- [x] Create Registration API View
- [x] Protect Views
- [x] Create Login view
- [ ] Create Password reset
- [x] Create Logout view
- [ ] Make custom perms
- [ ] Write tests
- [x] TestAPI's and populate test data
- [x] create comm channel app
- [x] Models for comm channel
- [x] Create Viewsets for comm channel
- [x] Create urls and router for comm channel
- [x] Create Pastor Dashboard
- [ ] Create comm channel UI
- [ ] Create Password reset 
- [ ] API for password reset
- [ ] Emailing feature

### Frontend
- [x] Landing page
- [x] Login page
- [x] Registration page
- [x] Comms page
- [x] Posting page
- [x] Home page
- [x] Seperate Home and landing page
- [ ] Create sidebar
- [x] create home page feed
- [ ] Create home page profile
- [ ] add upload button to home page

## Milestones
- [x] Full API Views
- [ ] Basic Dashboards
- [ ] Full test suite
- [ ] Dashboards
- [ ] Populate database
- [x] Member Groups
- [x] Communication Channel
- [ ] Full UI
- [ ] Deployment

## Suggestions
- Communication channel
- In app bible/hymnbook


## API Endpoints

/leadership-team
/age-group
/discipleship-group
/ropes-class
/serving-team
/ministry-data
/api/register
/api/posts
/api/comments
/profiles