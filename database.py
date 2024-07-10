import sqlite3
con = sqlite3.connect('employee.db')
print('Database connection established')

con.execute('CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email UNIQUE NOT NULL, address TEXT NOT NULL)')

print('Table created successfully')

con.close()
