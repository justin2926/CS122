from flask import Flask, g, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'messages.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               text TEXT
        )
    """)
    db.commit()

with app.app_context():
    init_db()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/add', methods=('GET', 'POST'))
def add_page():
    if request.method == 'POST':
        text = request.form['text']
        db = get_db()
        db.execute(
            'INSERT into messages (text) VALUES (?)', (text,)
        )
        db.commit()
        return redirect(url_for('add_page2'))
    return render_template('add.html')

@app.route('/add/success', methods=('GET', 'POST'))
def add_page2():
    if request.method == 'POST':
        text = request.form['text']
        db = get_db()
        db.execute(
            'INSERT into messages (text) VALUES (?)', (text,)
        )
        db.commit()
        return redirect(url_for('add_page2'))
    return render_template('add2.html')


@app.route('/view')
def view_page():
    db = get_db()
    messages = db.execute('SELECT id, text FROM messages').fetchall()
    return render_template('view.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)