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

## Technologies Used

- HTML: Used for creating the structure and layout of the web page.
- Flask: A Python web framework used for routing and rendering the dynamic web page.
- CSS: Used for styling the web page and adding visual enhancements.
- Jinja2: A templating engine used for integrating Python code with HTML templates.
-

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the application by executing `python app.py` in the terminal.
4. Open a web browser and navigate to `http://localhost:5000` to access the web application page.
5. From the options provided, choose the desired operation by clicking on the corresponding button.
6. Follow the prompts and input the required information to perform the selected operation.
7. View the results or feedback displayed on the web page.

Feel free to explore and utilize the different features of the web application page to manage student-related tasks efficiently.

## First Table
I made a table adding the col needed for students detale such as (First name,Last name, Date of birth, Address, email address, contact number, refrance no)

## Second Table
I needed to make a seperate table for students attendance containing details of the subjects they are attending and the date status of attendance. 

# design
I designed the webpage as simple as possible with green calming colors to not have negative effects on the users as colors effects mental health and as this webpage is only used for addministration work. as it was design to give comfortbal feeling while working with it.




## Attendance record website
 
## Target audience for web application
I originally created this project for school addministration works to deal with student ditals and mark their daily attendance. 
However,the users of this type of webpage are mostlly working for administration for companies or schools or even some businesses as they can addd data and update or remove it very easley.





#Testing
### description of test plan
### Test on different web browsers
* Safari
*  Chrome
*  Edge
###Lighthouse
### https://validator.w3.org
### jsLint.org

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
<!-- how to set up the program -->
# Deployment




# Heading 1
# Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6


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

