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

#insert data from add_student
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
    email=request.form['email']
    cur.execute('''INSERT INTO courses (first_name,last_name,gender,date_of_birth,phone_no,email) VALUES (%s,%s,%s,%s,%s,%s)''',(first_name,last_name,gender,date_of_birth,phone_no,email))
    conn.commit()
    cur.close()
    conn.close()
    #redirecting to a function called add_student
    return redirect(url_for('add_student'))
#search for student
@app.route("/search",methods=['POST'])
def search():
    conn=db_conn()
    cur=conn.cursor()
   # query="select * from courses where id=%s"
    #params=('lesly',)
    # first_name=request.form['fname']
    ID=request.form['id']
    # cur.execute('''select * from courses where first_name=%s''')
    cur.execute('''select * from courses where id='''+ID)
    #cur.execute('''select * from courses where id=%s''',ID)
    #print('''select * from courses where gender=%s''',ID)
    #cur.execute(query,params)
    data=cur.fetchall()
    # for row in rows:
    #     print(row)
    cur.close()
    conn.close()
    #render_template going to the template and finding the data and display it
    return  render_template("search_student.html", data=data)

#search student for update
@app.route("/search_update",methods=['POST'])
def search_update():
    conn=db_conn()
    cur=conn.cursor()
   # query="select * from courses where id=%s"
    #params=('lesly',)
    # first_name=request.form['fname']
    ID=request.form['id']
    # cur.execute('''select * from courses where first_name=%s''')
    cur.execute('''select * from courses where id='''+ID)
    #cur.execute('''select * from courses where id=%s''',ID)
    #print('''select * from courses where gender=%s''',ID)
    #cur.execute(query,params)
    data=cur.fetchall()
    # for row in rows:
    #     print(row)
    cur.close()
    conn.close()
    #render_template going to the template and finding the data and display it
    return  render_template("update_student.html", data=data)

#update student details
@app.route("/update",methods=['POST'])
def update():
    conn=db_conn()
    cur=conn.cursor()
    first_name=request.form['fname']
    # last_name=request.form['lname']
    # gender=request.form['gender']
    # date_of_birth=request.form['date_of_birth']
    # phone_no=request.form['phone']
    # email=request.form['email']
    id=request.form['id']
    # cur.execute('''UPDATE courses SET first_name=%s,last_name=%s,gender=%s,date_of_birth=%s,phone_no=%s,email=%s WHERE id=%s'''),(first_name,last_name,gender,date_of_birth,phone_no,email,id)
    cur.execute('''UPDATE courses SET first_name=%s WHERE id=%s''',(first_name,id))
    # commit the changes
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('update_student'))

#route to home webpage
@app.route("/index")
def index():
    return render_template("index.html")
#route to add student webpage
@app.route("/add_student")
def add_student():
    return render_template("add_student.html")
#route to search student webpage
@app.route("/search_student")
def search_student():
    return render_template("search_student.html")
    #route to search student webpage
@app.route("/update_student")
def update_student():
    return render_template("update_student.html")

if __name__ == '__main__':
    app.run(debug=True)
