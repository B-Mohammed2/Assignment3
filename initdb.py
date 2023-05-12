import psycopg2

conn=psycopg2.connect(database="flask_db3",host="localhost",user="postgres",password="Pass12",port="5432")

cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS courses(id serial PRIMARY KEY, name varchar(100),fees integer, duration integer);''')

cur.execute('''INSERT INTO courses(name,fees,duration) VALUES ('python', 6500,45),('javascript',6000,30);''')

conn.commit()

cur.close()

conn.close()
