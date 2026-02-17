<p align="center">
  <h3 align="center">Church Management System</h3>

  <p align="center">
    This is a simple django project made for Mavuno Young and Fearless and any other churches that might need a data management system. <br>
     This base version can be tweaked to fit most low church structures
    <br>
    </p>
</p>

<br>


## Table of contents
- [About](#about)
- [Technical](#technical)
- [Project Timeline](#project-timeline)
- [Using t](#project-timeline)
- [Licence](#license)
- [Contact Information](#contact-information)



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






### Contact Information

If you have found any bugs, or have any feedback or questions and or want to post a feature request please send an email at
bg1b9xany@mozmail.com

---
