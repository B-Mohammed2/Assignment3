import psycopg2

conn=psycopg2.connect(database="students_details",host="localhost",user="postgres",password="Pass12",port="5432")

cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS courses(id serial PRIMARY KEY, first_name varchar(100),last_name varchar(100)  );''')

cur.execute('''INSERT INTO courses(first_name,last_name) VALUES ('ab','ab');''')

conn.commit()

cur.close()

conn.close()
