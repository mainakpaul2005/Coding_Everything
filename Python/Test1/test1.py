from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

# Create the database and table if they don't exist
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Route to show the HTML form
@app.route('/')
def form():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']

    # Insert into DB
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (username,))
    conn.commit()
    conn.close()

    return redirect('/users')

# Route to display all users
@app.route('/users')
def show_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    html = "<h2>Submitted Users:</h2><ul>"
    for user in users:
        html += f"<li>{user[1]}</li>"
    html += "</ul><a href='/'>Go back</a>"

    return html

if __name__ == '__main__':
    app.run(debug=True)
