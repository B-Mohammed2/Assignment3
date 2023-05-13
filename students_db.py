from flask import Flask, render_template, redirect, request, url_for
import psycopg2
app=Flask(__name__)
#connecting to DB
def db_conn():
    conn=psycopg2.connect(database="students_details",host="localhost",user="postgres",password="Pass12",port="5432")
    return conn
#route to index.html
@app.route("/")
def homepage():
    return render_template("index.html") 
#route to add student webpage
@app.route("/add_student")
def add_student():
    return render_template("add_student.html")
@app.route("/create",methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    #variables to connect form with db
    first_name=request.form['fname']
    last_name=request.form['lname']
    gender=request.form['gender']
    date_of_birth=request.form['date_of_birth']
    phone_no=request.form['phone']
    cur.execute('''INSERT INTO courses (first_name,last_name,gender,date_of_birth,phone_no) VALUES (%s,%s,%s,%s,%s)''',(first_name,last_name,gender,date_of_birth,phone_no))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('add_student'))

if __name__ == '__main__':
    app.run(debug=True)
