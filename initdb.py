import psycopg2
#connect to db
conn=psycopg2.connect(database="students_details",host="localhost",user="postgres",password="Pass12",port="5432")

cur=conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS courses(id serial PRIMARY KEY, first_name varchar(100),last_name varchar(100),gender varchar(100),date_of_birth date, phone_no VARCHAR(14),email varchar(100) );''')
cur.execute('''CREATE TABLE IF NOT EXISTS courses(student_reference varchar(50) PRIMARY KEY, first_name varchar(100),last_name varchar(100),gender varchar(100),date_of_birth date, phone_no VARCHAR(14),email varchar(100) );''')
cur.execute('''INSERT INTO courses(student_reference,first_name,last_name,gender,date_of_birth,phone_no,email) VALUES ('00','ab','ab','ab','12-11-1999','00441234567890','ab@ab.com');''')

conn.commit()

cur.close()

conn.close()
