<h1 style="font-size: 24px;">Assignment3</h1>
<h2 style="font-size: 22px;">Student Records Management</h2>

live link to the website
https://record-wep-service.onrender.com

<h2 style="font-size: 22px;">Content</h2>

- [Introduction](#introduction)
  - [Features](#features)
  - [Target audience for web application](#target-audience-for-web-application)
- [User Stories](#user-stories)
  - [Technologies Used](#technologies-used)
  - [Frameworks, Libraries, and Programs used in this project are:](#frameworks-libraries-and-programs-used-in-this-project-are)
      - [Frameworks:](#frameworks)
      - [Libraries:](#libraries)
      - [Programs:](#programs)
      - [CSS and JavaScript:](#css-and-javascript)
- [Design](#design)
  - [SQL Database (PostgreSQL)](#sql-database-postgresql)
    - [First Table](#first-table)
    - [Second Table](#second-table)
  - [Wireframe](#wireframe)
- [Testing](#testing)
  - [Aoutomated tests](#aoutomated-tests)
    - [Lighthouse test](#lighthouse-test)
    - [Validation tests](#validation-tests)
      - [HTML Validation check](#html-validation-check)
      - [CSS Validation check](#css-validation-check)
      - [Python lint validation check](#python-lint-validation-check)
    - [Testing responsiveness](#testing-responsiveness)
      - [Manual test](#manual-test)
    - [Test on different web browsers](#test-on-different-web-browsers)
    - [Comment on the tests](#comment-on-the-tests)
  - [Test table](#test-table)
- [Video of the test](#video-of-the-test)
- [Bugs and problems encountered](#bugs-and-problems-encountered)
- [User manual](#user-manual)
- [Deployment](#deployment)
- [Security](#security)
    - [Acknowledgment](#acknowledgment)
    - [References](#references)
        - [bootstrap library](#bootstrap-library)
        - [Icone Website https://www.flaticon.com](#icone-website-httpswwwflaticoncom)
        - [bootstrap](#bootstrap)
        - [w3school](#w3school)
- [Code attribution](#code-attribution)


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

# User Stories

* As a user, I want to be able to add a new student to the database with their relevant details, such as their name, gender, date of birth, contact information, address, and next of kin information.
* As a user, I want to be able to search for a student in the database based on their first name and last name, or date of birth, or student reference number.
* As a user, I want to be able to update the details of a student in the database, including their name, gender, date of birth, contact information, address, and next of kin information.
* As a user, I want to be able to remove a student from the database along with their attendance records.
* As a user, I want to be able to view and update the attendance records of students for a particular day, specifying their attendance status for each student.
* As a user, I want to be able to search for a student's attendance records based on their first name, last name, date of birth, or student reference number.
* As a user, I want to be able to access a help section to understand how to use the application effectively.
* As a user, I want to be able to access information about the application and its purpose in an about section.

## Technologies Used

- HTML5: Used for creating the structure and layout of the web page. 
- CSS: Used for styling the web page and adding visual enhancements.
- Python: The programming language used for developing the backend logic of the application.
- PostgreSQL: A powerful open-source relational database management system used for storing and managing student details and attendance data.


## Frameworks, Libraries, and Programs used in this project are:

#### Frameworks:

Flask: A Python web framework used to provide tools and libraries for building web applications. It is used for routing, rendering templates, handling HTTP requests, and more.
#### Libraries:

psycopg2: A PostgreSQL adapter for Python, used for connecting to and interacting with the PostgreSQL database.
os: A module used for accessing the operating system functionalities, in this case, retrieving environment variables.

#### Programs:

PostgreSQL: A popular open-source relational database management system used as the backend database for this project.

#### CSS and JavaScript:

Bootstrap: A popular CSS framework used for styling the web application.
HTML:

Jinja2: A templating engine used in Flask for rendering dynamic content in HTML templates.


______

# Design
I designed the webpage with a clean and minimalist design, using soothing green colors to create a calm and comfortable environment for users. The purpose of the webpage is to serve as an administration tool, providing a pleasant and stress-free experience while performing administrative tasks. By using calming colors, the design aims to have a positive impact on users' mental well-being, promoting a sense of tranquility and ease while working with the webpage.

## SQL Database (PostgreSQL)
PostgreSQL is utilized as the database for this project. It incorporates two tables to enhance the functionality of the web application:

### First Table
The first table is designed to store student details and includes the following columns:
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
This table serves the purpose of storing and managing the personal information and contact details of students.

### Second Table

To facilitate the tracking of students' attendance, a separate table is created. This table consists of the following columns:

* Student ID: A unique identifier for each student.
* Subject: Details of the subjects or courses that students are attending.
* Date: The date on which the attendance is recorded.
* Attendance Status: The status of attendance for each student on a particular date.

This table allows you to keep a record of students' attendance for different subjects or courses, providing valuable information for monitoring and analyzing attendance patterns.


## Wireframe
| Desktop  | Tablet             | Smartpfhone|
| -------- | ------------------ |---------------------- |
|![](static/images/readme_file_image/wireframe/desktop.drawio.png)|![](static/images/readme_file_image/wireframe/tablet.drawio-2.png)|![](static/images/readme_file_image/wireframe/smartphone.drawio.png)|

_______

# Testing
The purpose of this Test Plan is to outline the testing approach and strategies for ensuring the proper functionality and usability of the web application. The test was devided by aoutomated and manual. Aoutomated tests included (lighthouse,code validation tests). furthumore, the web app was tested manually on different devices such as(Laptop, Tablet, smartphone) regarding responsiveness and functionality.
This Test Plan covers a range of test cases, including link navigation, verification of link text and images, and responsiveness across different screen sizes. By following this plan, I aim to identify any functional or usability issues, validate the correctness of the link destinations, and confirm that the web app behaves as expected in different environments.


## Aoutomated tests

### Lighthouse test
The web app was tested on Lighthouse for categories performance, accessibility, best practices, and SEO(Search Engine Optimization) for Mobile devices and Desktops. This is the report as in the images for all web pages:

|page|Desktop|Mobile|
|----|-------|------|
|Home|![](static/images/readme_file_image/lighthouse/desktop-index.png) | ![](static/images/readme_file_image/lighthouse/mobile-index.png)|
|Add student|![](static/images/readme_file_image/lighthouse/desktop-add.png) |![](static/images/readme_file_image/lighthouse/mobile_add.png)|
|Search for student|![](static/images/readme_file_image/lighthouse/desktop-search.png)|![](static/images/readme_file_image/lighthouse/mobile-search.png)|
|Update student detail|![](static/images/readme_file_image/lighthouse/desktop-update.png)|![](static/images/readme_file_image/lighthouse/mobile-update.png)|
|Delete student|![](static/images/readme_file_image/lighthouse/desktop-delete.png)|![](static/images/readme_file_image/lighthouse/mobile-delete.png)|
|Record Student Attendance|![](static/images/readme_file_image/lighthouse/desktop-register.png)|![](static/images/readme_file_image/lighthouse/mobile-register.png)|
|Search for student attendance|![](static/images/readme_file_image/lighthouse/desktop-reg-search.png)|![](static/images/readme_file_image/lighthouse/mobile-reg-search.png)|


### Validation tests
All the html codes and css codes was tested via W3C validator here is the results:

#### [HTML Validation check](https://validator.w3.org)
During the initial validation process, direct validation of the HTML code containing Jinja templates was not possible due to the presence of dynamic code elements. Therefore, the validation tests were conducted after deploying the web application. The validation process identified and corrected minor spelling errors, such as replacing '<lable>' with '<label>'. Additionally, it was discovered that using a link element '<a>' as a child element of a button element is not allowed, and this issue was resolved accordingly. Following the necessary fixes, the HTML code was revalidated and successfully passed the validation tests.
|page|validation Report|
|-----|---------------|
|Home |![](static/images/readme_file_image/validation/html%20validation/validate-index.png) |
|Add Student|![](static/images/readme_file_image/validation/html%20validation/validate-add-student.png) |
|Search Student|![](static/images/readme_file_image/validation/html%20validation/validate-search-student.png) |
|Update Student detail|![](static/images/readme_file_image/validation/html%20validation/validate-update.png) |
|Delete Student|![](static/images/readme_file_image/validation/html%20validation/validate-delete.png) |
|Record Student Attendance|![](static/images/readme_file_image/validation/html%20validation/validate-attendance.png)|
|Searching Student Attendance|![](static/images/readme_file_image/validation/html%20validation/validate-search-attendance.png)|
|Help|![](static/images/readme_file_image/validation/html%20validation/validate-help.png) |
|About Us|![](static/images/readme_file_image/validation/html%20validation/validate-about.png) |


#### [CSS Validation check](https://jigsaw.w3.org/css-validator/#validate_by_upload)

The CSS code was tested by uploading the file via validator. The result was No Errore found.

![](static/images/readme_file_image/validation/html%20validation/css-valid.png)


#### [Python lint validation check](https://infoheap.com/python-lint-online/)

The lint validation ensures that the Python code follows the correct syntax rules and helps identify any potential syntax errors or issues. The successful validation indicates that the code is written in a valid Python syntax according to the lint tool's standards.
![](static/images/readme_file_image/validation/html%20validation/pythonlint.png)


___

### Testing responsiveness
The responsiveness of the app was tested Manually on different devices and on google chrom developer tools responsiveness testing.
#### Manual test
the website was tested on different devices such as laptops, smartphones,tablets.
                         
|Device|test & Procedures|Home Page |Add Student page|Search Student page |Update student page |Delete Student page |Record Student Attendance|Search Student Attendance|Help page|About Us page|
|---|---|---|---|---|---|---|---|---|---|---|
|Laptop|Responsiveness|![](static/images/readme_file_image/manual-test/laptop/home.png)|![](static/images/readme_file_image/manual-test/laptop/add-student.png)|![](static/images/readme_file_image/manual-test/laptop/search-student.png)|![](static/images/readme_file_image/manual-test/laptop/update.png)|![](static/images/readme_file_image/manual-test/laptop/delete.png)|![](static/images/readme_file_image/manual-test/laptop/attendance.png)|![](static/images/readme_file_image/manual-test/laptop/search-attendance.png)|![](static/images/readme_file_image/manual-test/laptop/help.png)|![](static/images/readme_file_image/manual-test/laptop/about.png)|
|Tablet|Portrait mode|![](static/images/readme_file_image/manual-test/tablet/land/home.png)|![](static/images/readme_file_image/manual-test/tablet/land/add.png)|![](static/images/readme_file_image/manual-test/tablet/land/search.png)|![](static/images/readme_file_image/manual-test/tablet/land/update.png)|![](static/images/readme_file_image/manual-test/tablet/land/delete.png)|![](static/images/readme_file_image/manual-test/tablet/land/record.png)|![](static/images/readme_file_image/manual-test/tablet/land/search-att.png)|![](static/images/readme_file_image/manual-test/tablet/land/help.png)|![](static/images/readme_file_image/manual-test/tablet/land/about.png)|
|Tablet|Landscape mode|![](static/images/readme_file_image/manual-test/tablet/land/home.png)|![](static/images/readme_file_image/manual-test/tablet/land/add.png)|![](static/images/readme_file_image/manual-test/tablet/land/search.png)|![](static/images/readme_file_image/manual-test/tablet/land/update.png)|![](static/images/readme_file_image/manual-test/tablet/land/delete.png)|![](static/images/readme_file_image/manual-test/tablet/land/record.png)|![](static/images/readme_file_image/manual-test/tablet/land/search-att.png)|![](static/images/readme_file_image/manual-test/tablet/land/help.png)|![](static/images/readme_file_image/manual-test/smartphone/land/about.PNG)|
|Smartphone|Portrait mode|![](static/images/readme_file_image/manual-test/smartphone/potr/home.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/add.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/search.PNG) |![](static/images/readme_file_image/manual-test/smartphone/potr/update.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/delete.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/record.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/search-attendance.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/help.PNG)|![](static/images/readme_file_image/manual-test/smartphone/potr/about.PNG)|
|Smartphone|Landscape mode|![](static/images/readme_file_image/manual-test/smartphone/land/homa-land.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/add-land.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/search-.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/update.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/delete.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/record.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/search-attendance.PNG)|![](static/images/readme_file_image/manual-test/smartphone/land/help.png)|![](static/images/readme_file_image/manual-test/smartphone/land/about.PNG)|

### Test on different web browsers
* Safari
*  Chrome
*  Edge

### Comment on the tests
I noticed that the <input type="date"> displays the current date by default. However, in Chrome and Edge browsers, the format is displayed as (dd-mm-yyyy). It's important to note that the validation doesn't accept the placeholder attribute for the date input. Additionally, adding a placeholder doesn't affect the way the date is displayed in the input field.


## Test table

<!-- Tables -->

| Page Name| Test Procedures| Expected Outcome | Actual Outcome  |
| ------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| Home Page                | a. Click on the logo "MANAGING STUDENTS RECORDS" link.                    | Navigate to the home page from any page of the web app.               | The home page opens.                                            |
|                          | b. Verify that the page loads correctly.                                   | The page opens with the expected layout and elements.                  | The page displays as expected.                                  |
| Add Students             | a. Click on the "Add Students" link.                                       | Open the "Add Student" page.                                          | The "Add Student" page is displayed.                            |
|                          | b. Verify that the page loads correctly.                                   | The page opens with the expected form and layout.                      | The page displays the "Add Student" form as expected.           |
|                          | c. Fill in the required information in the form.                           | All fields accept the required data.                                  | All fields can be filled as desired.                            |
|                          | d. Click the "Add Student" button.                                         | The form is submitted successfully.                                   | The form is submitted and data is sent to the database.         |
|                          | e. Verify that the student is successfully added to the database.          | The entered data is displayed in the correct database column.         | The data is entered correctly in the database.                  |
| Search for Student       | a. Click on the "Search for student" link.                                 | Open the "Search for student" page.                                   | The "Search for student" page is displayed.                     |
|                          | b. Verify that the page loads correctly.                                   | The page opens with the expected form and layout.                      | The page displays the "Search for student" form as expected.    |
|                          | c. Enter the student details or search criteria.                           | All fields accept the required data.                                  | All fields can be filled as needed.                             |
|                          | d. Click the "Search" button.                                              | The form is submitted successfully.                                   | The form is submitted and data is retrieved from the database.  |
|                          | e. Verify that the search results are displayed correctly.                  | The data is displayed correctly in a table format.                    | The search results are displayed accurately.                    |
| Update Student Details   | a. Click on the "Update student detail" link.                              | Open the "Update student" page.                                       | The "Update student" page is displayed.                         |
|                          | b. Verify that the page loads correctly.                                   | The page opens with the expected form and layout.                      | The page displays the "Update student" form as expected.        |
|                          | c. Click the "Search" button.                                              | The form is submitted successfully.                                   | The form is submitted and data is retrieved from the database.  |
|                          | d. Verify that the search results are displayed correctly.                  | The data is displayed correctly in the fields.                         | The data is displayed accurately.                              |
|                          | e. Edit the student details as required.                                   | The fields can be edited.                                             | The details can be changed.                                     |
|                          | f. Click the "Update" button.                                              | The form is submitted successfully.                                   | The form is submitted and data is sent to the database.         |
|                          | g. Verify that the student's details are successfully updated.             | The details are updated properly.                                     | The data is displayed correctly in the table.                   |
| Delete Student           | a. Click on the "Delete student" link.                                     | Open the "Delete student" page.                                       | The "Delete student" page is displayed.                         |
|                          | b. Verify that the page loads correctly.                                   | The page opens with the expected form and layout.                      | The page displays the "Delete student" form as expected.        |
|                          | c. Find the student to delete from the search form.                        | The details of the searched student appear after clicking "Search".   | The selected student details are displayed.                     |
|                          | d. Click the "Delete" button.                                              | The selected student details are removed from the system.             | The student is successfully removed.                            |
|                          | e. Verify that the student is successfully deleted from the database.      | Searching for the student displays "NO Student Found".                | "No Student Found" is displayed when searching for the student. |
| Record Student Attendance | a. Click on the "Record Student Attendance" link.                    | Open the "Record Student Attendance" page.                            | The "Record Student Attendance" page is displayed.           |
|                            | b. Verify that the page loads correctly.                              | The page opens with the expected subject input and a table of students. | The page displays the subject input and table as expected.   |
|                            | c. Mark attendance using the radio buttons.                           | The student records are marked as attended or not attended.            | Attendance recording is successful.                          |
|                            | d. Write the subject name.                                           | The subject name is recorded in the designated field.                 | It works as expected.                                        |
|                            | e. Click the "Submit" button.                                        | The attendance data is added to the Attendance table.                 | The data is successfully added.                              |
|                            | f. Verify that the attendance is recorded successfully.              | The data is added to the database and can be confirmed in searches.   | The attendance is recorded successfully.                     |
| Search Student Attendance  | a. Click on the "Search Student Attendance" link.                    | Open the "Search Student Attendance" page.                            | The "Search Student Attendance" page is displayed.           |
|                            | b. Verify that the page loads correctly.                              | The page opens with the search form to select a student.               | The page displays as expected.                               |
|                            | c. Enter the student details or search criteria.                      | Find the student details using any of the provided methods.            | The student is found using different search methods.         |
|                            | d. Click the "Search" button.                                         | Submit the search form and display the data.                          | The data is displayed as requested.                          |
|                            | e. Verify that the attendance records are displayed correctly.        | The selected student's attendance records are displayed.               | The data is displayed accurately.                            |
| Help page                  | a. Click on the "Help" link.                                          | Open the Help page.                                                    | The Help page is displayed.                                  |
|                            | b. Verify that the page loads correctly.                              | The page displays the expected help guidelines for the web app.        | The page is displayed as expected.                           |
| About us page              | a. Click on the "About us" link.                                      | Open the About us page.                                                | The About us page is displayed.                              |
|                            | b. Verify that the page loads correctly.                              | The page displays the expected information.                            | The page is displayed as expected.                           |



# Video of the test
https://record-wep-service.onrender.com/video



# Bugs and problems encountered

|Issue    |	Description	       |Solution |
| --------| ------------------ |-------- |
|Inserting data without committing|	Forgot to commit the database transaction after inserting data into a table.|	Ensure to commit the transaction after executing the insert command.|
|Linking CSS and image files|Encountered issues with linking CSS and image files to the website.|	Use the URL method and place all the CSS and image files in the static folder of the web application.|
|Searching for students without Date of Birth|The program crashes when searching for students without providing the Date of Birth.|	Implement an if statement to handle searching with or without the Date of Birth.|
|Handling student details separately in attendance table|Faced difficulty in displaying student details separately from the attendance table to avoid repetition.|	Use conditional statements (e.g., if statement) in Jinja template to show the page without crashing and display the student details when searched for.|
|Multiple data shown when searching attendance by Student ID|When searching for student attendance records by Student ID, multiple records were displayed.|	Modify the SQL query in Python to fetch only the relevant attendance record for the given Student ID.|
|Case sensitivity in search |Search doesn't find data if the input wasn't in the same capitalization as the data in SQL.|Fix by adding the UPPER function to the SQL query to make the search case-insensitive.|

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
6.  autopep8: pip install -U autopep8


<!-- how to set up the program -->
# Deployment

First: Create a Render account.
Second: Set up a PostgreSQL database on Render.
Third: Create a web service.
   1. Connect with GitHub and authorize the connection.
   2. Install Render in GitHub.
   3. Connect with the repository.
   4. Install Gunicorn.
   5. Generate a requirements.txt file using pip.
    
Fourth: Configure the PostgreSQL administration tool.
  * Access the server dialog to describe the connection to a server.For connections in pgAdmin from outside, use the steps in this page: http://127.0.0.1:62055/help/help/server_dialog.html.
  

# Security
To hide sensitive information such as passwords and usernames in a Python application, I used 'os' moudle. This is the process:
First: Import the 'os' module at the top of python file.

Second: Set the sensitive information as environment variables and  give values to the environment variables in sql terminal. for example:

export MY_USERNAME="your_username"
export MY_PASSWORD="your_password"

Third: Access the environment variables in the code wherever needed by only typing the environment value given as the username or password.

'your_username'=os.environ.get['MY_USERNAME'] 
'your_password'=os.environ.get['MY_PASSWORD'] 

this methode allows you to store sensitive information as environment variables and not hardcoded within your code to enhance data protection and security.



### Acknowledgment



### References
##### bootstrap library
##### Icone Website https://www.flaticon.com
##### bootstrap 
##### w3school


# Code attribution




