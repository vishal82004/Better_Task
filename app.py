from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3 as sql


app = Flask(__name__)

# Main Route
@app.route('/')

# Read Operation
@app.route('/index')
def index():
    con = sql.connect('employee.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    fetch_data = cur.fetchall()
    return render_template('index.html', data = fetch_data)


# Create Operation
@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO employee (name, email, address) VALUES (?, ?, ?)", (name, email, address))
            con.commit()
            flash("Record successfully added")
            return redirect(url_for('index'))
       
    return render_template('add_user.html')

# Update operation
@app.route('/edit_user/<string:id>', methods=['POST', 'GET'])
def edit_user(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute("UPDATE employee SET name=?, email=?, address=? WHERE id=?", (name, email, address, id))
            con.commit()
            flash("Record successfully edited")
            return redirect(url_for('index'))
    con = sql.connect('employee.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM employee WHERE id=?", (id,))
    data = cur.fetchone()
    return render_template('edit_user.html', data=data)
            

# Delete operation
@app.route('/delete_user<string:id>', methods=['GET'])
def delete_user(id):
    con = sql.connect('employee.db')
    cur = con.cursor()
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    con.commit()
    flash("Record successfully deleted")
    return redirect(url_for('index'))

# search operation
@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']
    con = sql.connect('employee.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM employee WHERE name LIKE?", ('%'+search_term+'%',))
    fetch_data = cur.fetchall()
    return render_template('index.html', data = fetch_data)



                            



if __name__ == '__main__':
    app.secret_key='aqueeq1997'
    app.run(host="0.0.0.0", port=5000, debug=True)
