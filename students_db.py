import os
from flask import Flask, render_template, redirect, request, url_for
import psycopg2
user_db=os.environ.get('DB_USER')
password_db=os.environ.get('DB_PASS')
app=Flask(__name__)

#connecting to DB
def db_conn():
    conn=psycopg2.connect(database="students_details", host="dpg-cijuec5ph6euh7if58e0-a", user=user_db, password=password_db, port="5432")
    return conn

#route to index.html
@app.route("/")
def homepage():
    return render_template("index.html") 
#route to home webpage
@app.route("/index")
def index():
    return render_template("index.html")


#route to add student webpage
@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


#insert data from add_student
@app.route("/create",methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    #variables to connect form with db
    student_reference=request.form['st_ref']
    first_name=request.form['fname']
    last_name=request.form['lname']
    gender=request.form['gender']
    date_of_birth=request.form['date_of_birth']
    phone_no=request.form['phone']
    email=request.form['email']
    address=request.form['first_line'] +'  ' + request.form['second_line'] + '  '+ request.form['city'] + '  ' +request.form['postcode']
    next_kin=request.form['kin_fname'] +'  ' + request.form['kin_lname']
    kin_rel=request.form['kin_relationship']
    kin_no=request.form['kin_phone']
    kin_email=request.form['kin_email']
    sql_add = "INSERT INTO courses (student_reference, first_name, last_name, gender, date_of_birth, phone_no, email, address, kin_full_name, kin_relationship, kin_phone, kin_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (student_reference, first_name, last_name, gender, date_of_birth, phone_no, email, address, next_kin, kin_rel, kin_no, kin_email)
    cur.execute(sql_add, data)
    conn.commit()
    cur.close()
    conn.close()
    #redirecting to a function called add_student
    return redirect(url_for('add_student'))

#route to search student webpage 
@app.route("/search_student")
def search_student():
    return render_template("search_student.html")

#search for student
@app.route("/search",methods=['POST'])
def search():
    conn=db_conn()
    cur=conn.cursor()
    first_name=request.form['fname'].upper()
    last_name=request.form['lname'].upper()
    date_of_birth=request.form['birth_date']
    ID=request.form['id']
    #joinn strings (id and st_ref togehter (concatenation)  
    print("dateofbirth is" + date_of_birth)
    if date_of_birth =='':
        search_string="select * from courses where upper(first_name)='"+first_name+"' And upper(last_name)='"+last_name+"' OR student_reference='"+ID+"' ;"
    else:
        search_string="select * from courses where upper(first_name)='"+first_name+"' And upper(last_name)='"+last_name+"' OR student_reference='"+ID+"' OR date_of_birth='"+date_of_birth+"' ;"

    cur.execute(search_string)
    data=cur.fetchall()
    cur.close()
    conn.close()
    #render_template going to the template and finding the data and display it
    return  render_template("search_student.html", data=data)
    



# Route to update student webpage
@app.route("/update_student")
def update_student():
    return render_template("update_student.html")

# Search student for update
@app.route("/search_update", methods=['GET', 'POST'])
def search_update():
    if request.method == 'POST':
        conn = db_conn()
        cur = conn.cursor()
        first_name = request.form['fname']
        last_name = request.form['lname']
        date_of_birth = request.form['birth_date']
        ID = request.form['id']

        if date_of_birth == '':
            search_string = "SELECT * FROM courses WHERE first_name=%s AND last_name=%s OR student_reference=%s;"
            params = (first_name, last_name, ID)
        else:
            search_string = "SELECT * FROM courses WHERE first_name=%s AND last_name=%s OR student_reference=%s OR date_of_birth=%s;"
            params = (first_name, last_name, ID, date_of_birth)

        cur.execute(search_string, params)
        data = cur.fetchall()

        cur.close()
        conn.close()

        return render_template("update_student.html", data=data)
    else:
        return redirect(url_for('update_student'))

# Update student details
@app.route("/update", methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()

    first_name = request.form['fname']
    last_name = request.form['lname']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    phone_no = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    next_kin = request.form['kin_full_name']
    relationship = request.form['relationship']
    kin_phone = request.form['kin_phone']
    kin_email = request.form['kin_email']
    ID= request.form['id']

    sql_update = '''UPDATE courses SET first_name=%s, last_name=%s, gender=%s, date_of_birth=%s, phone_no=%s, email=%s, address=%s, kin_full_name=%s, kin_relationship=%s, kin_phone=%s, kin_email=%s WHERE student_reference=%s'''
    params = (first_name, last_name, gender, date_of_birth, phone_no, email, address, next_kin, relationship, kin_phone, kin_email, ID)

    cur.execute(sql_update, params)
    print(sql_update)
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('update_student'))



#route to delete student webpage
@app.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")


#search student for delete
@app.route("/search_delete",methods=['POST'])
def search_delete():
    conn=db_conn()
    cur=conn.cursor()
    first_name=request.form['fname']
    last_name=request.form['lname']
    date_of_birth=request.form['birth_date']
    ID=request.form['id']
    #joinn strings (id and st_ref togehter (concatenation)  
    if date_of_birth =='':
        search_string="select * from courses where first_name='"+first_name+"' And last_name='"+last_name+"' OR student_reference='"+ID+"' ;"
    else:
        search_string="select * from courses where first_name='"+first_name+"' And last_name='"+last_name+"' OR student_reference='"+ID+"' OR date_of_birth='"+date_of_birth+"' ;"

    cur.execute(search_string)
    data=cur.fetchall()
    cur.close()
    conn.close()
    #render_template going to the template and finding the data and display it
    return  render_template("delete_student.html", data=data)


#Delet Student
@app.route("/delete",methods=['POST'])
def delete():
    conn=db_conn()
    cur=conn.cursor()
    ID=request.form['id']
    # we need to delete the data from both table.if a student detail was deleted from main table
    # the related table will be left without connected data and will face error.
    cur.execute('''DELETE FROM attendance  WHERE student_reference=%s''', (ID,))
    cur.execute('''DELETE FROM courses  WHERE student_reference=%s''', (ID,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))



#this part is for students Attendance
#route to attendance_student webpage
@app.route("/attendance_student")
def attendance_student():
    conn=db_conn()
    cur=conn.cursor()
    #retrieve all records from attendance table where date of attendance is today
    cur.execute("select * from attendance where date_of_attendance=CURRENT_DATE;")
    #if no records where retrived then
    if cur.rowcount==0:
        cur.execute("select * from courses")
    #creat todays register
        studentdata=cur.fetchall()
        for x in studentdata:
            sql_test="INSERT INTO attendance(subject,student_reference,attendance) VALUES (null,'"+x[0]+"',null);"
            cur.execute(sql_test)
            conn.commit()
    # making relationship between the two tables using the student reference number and adding a condition for the date of attendance to avoid duplicate.
    search_string="select * from courses, attendance where courses.student_reference=attendance.student_reference AND attendance.date_of_attendance=CURRENT_DATE order by attendance_id ASC;"
    cur.execute(search_string)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return render_template("attendance_student.html", data=data)

#creating daily attendance in register page
@app.route("/create_attendance",methods=['POST'])
def create_attendance():
    conn=db_conn()
    cur=conn.cursor()
    #variables to connect form with db
    #variable to request data structured in  alist from form(convert data to dictionary type)
    #reasult givs attendance record
    result=request.form.to_dict(flat=False)
    #to list the keys in to col values to show one item
    keylist=list(result.keys())
    valuelist=list(result.values())
    number_of_records=len(keylist)
    for current_attendance_record in range(number_of_records-1):
        #update for attendance
        sql_update_attendance="UPDATE attendance SET attendance='"+valuelist[current_attendance_record+1][0]+"' where student_reference='"+keylist[current_attendance_record+1]+"' AND attendance.date_of_attendance=CURRENT_DATE;"
        #update for subject
        sql_update_subject="UPDATE attendance SET subject='" + valuelist[0][0] + "' where student_reference='"+keylist[current_attendance_record+1]+"' AND attendance.date_of_attendance=CURRENT_DATE;"
        cur.execute(sql_update_attendance)
        cur.execute(sql_update_subject)
        conn.commit()

    cur.close()
    conn.close()
    #redirecting to a function called add_student
    return redirect(url_for('attendance_student'))

#route to search_attendance_student webpage
@app.route("/search_attendance_student")
def search_attendance_student():
    return  render_template("search_student_attendance.html")
    

@app.route("/search_student_attendance", methods=['POST'])
def search_student_attendance_detail():
    conn = db_conn()
    cur = conn.cursor()
    first_name = request.form['fname']
    last_name = request.form['lname']
    ID = request.form['id']
    date_of_birth = request.form['birth_date']
    #joinn strings (id and st_ref togehter (concatenation)
    if date_of_birth == '':
        # Search by name and ID
        search_query = "SELECT * FROM courses, attendance WHERE courses.student_reference=attendance.student_reference AND (courses.first_name=%s AND courses.last_name=%s OR courses.student_reference=%s);"
        cur.execute(search_query, (first_name, last_name, ID))
    else:
        # Search by name and date of birth
        search_query = "SELECT * FROM courses, attendance WHERE courses.student_reference=attendance.student_reference AND courses.first_name=%s AND courses.last_name=%s AND courses.date_of_birth=%s;"
        cur.execute(search_query, (first_name, last_name, date_of_birth))

    data = cur.fetchall()
    cur.close()
    conn.close()
    #render_template going to the template and finding the data and display it
    return render_template("search_student_attendance.html", data=data)

@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
