from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DATABASE = 'data.db'
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute
    conn.commit()
    conn.close()
def insert_submission(name, email):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO submissions (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
def get_all_submissions():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT id, name, email FROM submissions')
    rows = c.fetchall()
    conn.close()
    return rows
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            insert_submission(name, email)
            return redirect(url_for('display'))
    return render_template('form.html')
@app.route('/display')
def display():
    entries = get_all_submissions()
    return render_template('display.html', entries=entries)
if __name__ == '__main__':
    init_db()
    app.run(debug=False)
