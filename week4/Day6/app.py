from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute
    conn.commit()
    conn.close()
init_db()
@app.route('/')
def list():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    conn.close()
    return render_template("list.html", employees=data)
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employee(name,email,phone,department) VALUES(?,?,?,?)",
                       (name,email,phone,department))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template("add.html")
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']
        cursor.execute("UPDATE employee SET name=?,email=?,phone=?,department=? WHERE id=?",
                       (name,email,phone,department,id))
        conn.commit()
        conn.close()
        return redirect('/')
    cursor.execute("SELECT * FROM employee WHERE id=?", (id,))
    employee = cursor.fetchone()
    conn.close()
    return render_template("edit.html", emp=employee)
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)