# Assignment3
Student Records Management

live link to the website
https://record-wep-service.onrender.com

# Table of content
[Introduction](#Introduction)
[Features](#Features)
[User Stories](#User-Stories)
[Technologies Used](#Technologies-Used)
[Design](#Design)
[Wireframe](#Wireframe)
[Testing](#Testing)
[]

<!-- Introduction -->
# Introduction 
This is a web application page that allows you to perform various operations related to student management. It provides the following features:

## Features

- Add Students: add new students to the system by filling out the form on the "Add Student" page.
- Search for Students:search and retrieve student details using their full name, ID number, or date of birth.
- Update Student Details: Seamlessly update the information of existing students as needed.
- Delete Students: Conveniently remove a student from the system when necessary.
- Student Attendance Register: Maintain and manage daily attendance records for students.
View Student Attendance: Quickly search and view the daily attendance records of students.

## Target audience for web application
I originally created this project for school addministration works to deal with student ditals and mark their daily attendance. 
However,the users of this type of webpage are mostlly working for administration for companies or schools or even some businesses as they can addd data and update or remove it very easley.

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


# Design
I designed the webpage with a clean and minimalist design, using soothing green colors to create a calm and comfortable environment for users. The purpose of the webpage is to serve as an administration tool, providing a pleasant and stress-free experience while performing administrative tasks. By using calming colors, the design aims to have a positive impact on users' mental well-being, promoting a sense of tranquility and ease while working with the webpage.

## Wireframe
| Desktop  | Tablet             | Smartpfhone|
| -------- | ------------------ |---------------------- |
|![](static/images/readme_file_image/wireframe/desktop.drawio.png)|![](static/images/readme_file_image/wireframe/tablet.drawio-2.png)|![](static/images/readme_file_image/wireframe/smartphone.drawio.png)|

## Testing
The purpose of this Test Plan is to outline the testing approach and strategies for ensuring the proper functionality and usability of the web application. The test was devided by aoutomated and manual. Aoutomated tests included (lighthouse,code validation tests). furthumore, the web app was tested manually on different devices such as(Laptop, Tablet, smartphone) regarding responsiveness and functionality.


#### Aoutomated tests

### Lighthouse test
The web app was tested on Lighthouse for categories performance, accessibility, best practices, and SEO(Search Engine Optimization) for Mobile devices and Desktops. This is the report as in the images for all web pages:

|page|Desktop|Mobile|
|----|-------|------|
|Home|![](static/images/readme_file_image/lighthouse/desktop-index.png) | ![](static/images/readme_file_image/lighthouse/mobile-index.png)|
|Add student|![](static/images/readme_file_image/lighthouse/desktop-add.png) |![](static/images/readme_file_image/lighthouse/mobile_add.png)|
|Search for student|![](static/images/readme_file_image/lighthouse/desktop-search.png)|![](static/images/readme_file_image/lighthouse/mobile-search.png)|
|Update student detail|![](static/images/readme_file_image/lighthouse/desktop-update.png)|![](static/images/readme_file_image/lighthouse/mobile-update.png)|
|Delete student|![](static/images/readme_file_image/lighthouse/desktop-delete.png)|![](static/images/readme_file_image/lighthouse/mobile-delete.png)|
|Student daily register|![](static/images/readme_file_image/lighthouse/desktop-register.png)|![](static/images/readme_file_image/lighthouse/mobile-register.png)|
|Search for student attendance|![](static/images/readme_file_image/lighthouse/desktop-reg-search.png)|![](static/images/readme_file_image/lighthouse/mobile-reg-search.png)|


### Validation tests
All the html codes and css codes was tested via W3C validator here is the results:

#### [HTML validator](https://validator.w3.org)
During the initial validation process, direct validation of the HTML code containing Jinja templates was not possible due to the presence of dynamic code elements. Therefore, the validation tests were conducted after deploying the web application. The validation process identified and corrected minor spelling errors, such as replacing '<lable>' with '<label>'. Additionally, it was discovered that using a link element '<a>' as a child element of a button element is not allowed, and this issue was resolved accordingly. Following the necessary fixes, the HTML code was revalidated and successfully passed the validation tests.
|page|validation Report|
|-----|---------------|
|Home |![](static/images/readme_file_image/validation/html%20validation/validate-index.png) |
|Add Student|![](static/images/readme_file_image/validation/html%20validation/validate-add-student.png) |
|Search Student|![](static/images/readme_file_image/validation/html%20validation/validate-search-student.png) |
|Update Student detail|![](static/images/readme_file_image/validation/html%20validation/validate-update.png) |
|Delete Student|![](static/images/readme_file_image/validation/html%20validation/validate-delete.png) |
|Student daily register|![](static/images/readme_file_image/validation/html%20validation/validate-attendance.png)|
|Searching Student Attendance|![](static/images/readme_file_image/validation/html%20validation/validate-search-attendance.png)|
|Help|![](static/images/readme_file_image/validation/html%20validation/validate-help.png) |
|About Us|![](static/images/readme_file_image/validation/html%20validation/validate-about.png) |


#### [CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_upload)
The CSS code was tested by uploading the file via validator. The result was No Errore found.

![](static/images/readme_file_image/validation/html%20validation/css-valid.png)


### Test on different web browsers
* Safari
*  Chrome
*  Edge














The web app provides various features and functionalities such as adding students, searching for students, updating student details, deleting students, and managing student attendance records. The goal of testing is to ensure that users can navigate through the application seamlessly, perform the intended actions, and have a positive user experience.

This Test Plan covers a range of test cases, including link navigation, verification of link text and images, and responsiveness across different screen sizes. By following this plan, we aim to identify any functional or usability issues, validate the correctness of the link destinations, and confirm that the web app behaves as expected in different environments.

## Test table
<!-- Tables -->
| Test No | Purpose            | Test and Or data|Expected Outcome|Actual Outcome|Comments|
| --------| ------------------ |-------- |--------|--------|--------|
| 5       | install psycopg2  |         |        |        |for mac user add binary in th end|




# Bugs and problems encountered

|Issue    |	Description	       |Solution |
| --------| ------------------ |-------- |
|Inserting data without committing|	Forgot to commit the database transaction after inserting data into a table.|	Ensure to commit the transaction after executing the insert command.|
|Linking CSS and image files|Encountered issues with linking CSS and image files to the website.|	Use the URL method and place all the CSS and image files in the static folder of the web application.|
|Searching for students without Date of Birth|The program crashes when searching for students without providing the Date of Birth.|	Implement an if statement to handle searching with or without the Date of Birth.|
|Handling student details separately in attendance table|Faced difficulty in displaying student details separately from the attendance table to avoid repetition.|	Use conditional statements (e.g., if statement) in Jinja template to show the page without crashing and display the student details when searched for.|
|Multiple data shown when searching attendance by Student ID|When searching for student attendance records by Student ID, multiple records were displayed.|	Modify the SQL query in Python to fetch only the relevant attendance record for the given Student ID.|


## references
### Icone Website https://www.flaticon.com
### bootstrap 
### w3school

# Security

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

## SQL 
I have designed a database with two tables to enhance the functionality of the web application:

### First Table

I have created a table that includes the following columns for student details:

* First Name
* Last Name
* Date of Birth
* Address
* Email Address
* Contact Number
* Next of Kin
* Relationship to Next of Kin
* Next of Kin's Phone Number
* Next of Kin's Email
* Reference Number
This table is designed to store and manage the personal information and contact details of students.

### Second Table

To track students' attendance, I have created a separate table. This table includes the following columns:

* Student ID: A unique identifier for each student.
* Subject: Details of the subjects or courses that students are attending.
* Date: The date on which the attendance is recorded.
* Attendance Status: The status of attendance for each student on a particular date.
This table allows you to keep a record of students' attendance for different subjects or courses, providing valuable information for monitoring and analyzing attendance patterns.

<!-- how to set up the program -->
# Deployment
1. creat render account
2. creat postgrasql database in render
3. creat webservice
connect with gethub and outhorize it
install render in github
get all the reposetries from github
connect with the reposetry
instal gunicorn
 make pip >requirments.txt
4. pg admine 
image
explening Use the Server dialog to describe a connection to a server:
http://127.0.0.1:62055/help/help/server_dialog.html
 when connecting from outside 




testing
search doesn't find data if the input was not capitalasation wasn't as data in sql. fixed by adding upper function.






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

