# Assignment3
Student Records Management
<!-- Introduction -->
# Introduction 
This is a web application page that allows you to perform various operations related to student management. It provides the following features:

## Features
- Add Students: Add new students to the system from add student page.
- Search for Student: Search and retrieve student details based on different using different methods.
- Update Student Detail: Update the details of existing students.
- Delete Student: Remove a student from the system.
- Student's Daily Register: Record and manage daily attendance records for students.
- Student's Daily Attendance: Search and view the daily attendance records of students.


## User Stories

* As a user, I want to be able to add a new student to the database with their relevant details, such as their name, gender, date of birth, contact information, address, and next of kin information.
* As a user, I want to be able to search for a student in the database based on their first name and last name, or date of birth, or student reference number.
* As a user, I want to be able to update the details of a student in the database, including their name, gender, date of birth, contact information, address, and next of kin information.
* As a user, I want to be able to remove a student from the database along with their attendance records.
* As a user, I want to be able to view and update the attendance records of students for a particular day, specifying their attendance status for each student.
* As a user, I want to be able to search for a student's attendance records based on their first name, last name, date of birth, or student reference number.
* As a user, I want to be able to access a help section to understand how to use the application effectively.
* As a user, I want to be able to access information about the application and its purpose in an about section.

## Technologies Used

- HTML: Used for creating the structure and layout of the web page.
- Flask: A Python web framework used to provide tools and libraries for building web applications. It is used for routing, rendering templates, handling HTTP requests, and more.
- CSS: Used for styling the web page and adding visual enhancements.
- Jinja2: A templating engine used for integrating Python code with HTML templates.
- Python: The programming language used for developing the backend logic of the application.
- PostgreSQL: A powerful open-source relational database management system used for storing and managing student details and attendance data.
- Psycopg2: A PostgreSQL adapter for Python that allows Python programs to access a PostgreSQL database. It is used to establish a connection between the Flask application and the PostgreSQL database.

Feel free to explore and utilize the different features of the web application page to manage student-related tasks efficiently.

## First Table
I made a table adding the col needed for students detale such as (First name,Last name, Date of birth, Address, email address, contact number, refrance no)

## Second Table
I needed to make a seperate table for students attendance containing details of the subjects they are attending and the date status of attendance. 

# design
I designed the webpage as simple as possible with green calming colors to not have negative effects on the users as colors effects mental health and as this webpage is only used for addministration work. as it was design to give comfortbal feeling while working with it.

## Wireframe
| Desktop  | Tablet             | Smartpfhone|
| -------- | ------------------ |---------------------- |
|![](static/images/readme_file_image/wireframe/desktop.drawio.png)|![](static/images/readme_file_image/wireframe/tablet.drawio-2.png)||![](static/images/readme_file_image/wireframe/smartphone.drawio.png)

## Attendance record website
 
## Target audience for web application
I originally created this project for school addministration works to deal with student ditals and mark their daily attendance. 
However,the users of this type of webpage are mostlly working for administration for companies or schools or even some businesses as they can addd data and update or remove it very easley.


# Testing
### description of test plan
### Test on different web browsers
* Safari
*  Chrome
*  Edge

### Lighthouse

### https://validator.w3.org


## Test table
<!-- Tables -->
| Test No | Purpose            | Test and Or data|Expected Outcome|Actual Outcome|Comments|
| --------| ------------------ |-------- |--------|--------|--------|
| 5       | install psycopg2  |         |        |        |for mac user add binary in th end|




# Bugs and problems encountered
one of the issuse i face was I tried to cary a command to insert a data into a table then i found out i forgot to commit it. Another chalenge was linking (css,img) files to the website as it wasn't finding it so I tried to use url method and put all the files in static folder. I had another problem in searching for students.the program was crashing whenever I search without the date of birth.Therefore,I used if function to work with and without date of birth.
In searching attendance student, I had problem with defining data when I tried to get student details to show out of the table seperatly for it not to be repeated with table with each attendance. I fixed it by useing if jinja to show the page without crashing and show the results whenever searched for data. 

## references
### Icone Website https://www.flaticon.com
### bootstrap 
### w3school

#Security

# Code attribution
## e.g. bootstrap library

# Screenshots

<!-- how to use the application -->
# User manual

Before running the application, make sure you have the following:
Python 3 installed on your system
PostgreSQL database created on your local machine
In the terminal follow these steps: 
1. pip3 install virtualenv
2. Name the virtualenv : virtualenv 'Name'env
3. Activate virtualenv : ('Name'env/bin/activate)
For Mac (source  'Name'env/bin/activate)
4. pip3 install flask
5. install psycopg2 (pip3 install psycopg2)For Mac (pip3 install psycopg2-binary)
Required Python packages installed. You can install them by running the following command:

<!-- how to set up the program -->
# Deployment







<!-- Italics -->
*This text* is italic

_This text_ is italic

<!-- Strong -->
**This text** is italic

__This text__ is italic

<!-- Strikethrough -->
~~This text~~ is strikethrough

<!-- Horizontal Rule -->

---
___

<!-- Blockquote -->
> This is a quote

<!-- Links -->
[Traversy Media](http://www.traversymedia.com)

[Traversy Media](http://www.traversymedia.com "Traversy Media")

<!-- UL -->
* Item 1

