import psycopg2

conn=psycopg2.connect(database="students_details",host="localhost",user="postgres",password="Pass12",port="5432")

cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS courses(id serial PRIMARY KEY, first_name varchar(100),last_name varchar(100),gender varchar(100),date_of_birth date, phone_no VARCHAR(14) );''')

cur.execute('''INSERT INTO courses(first_name,last_name,gender,date_of_birth,phone_no) VALUES ('ab','ab','ab','12-11-1999','00441234567890');''')

conn.commit()

cur.close()

conn.close()
