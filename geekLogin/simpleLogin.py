from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import json


app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

parametros = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'geekLogin.ini'))
with open(parametros, 'r') as f:
    conArgs = json.load(f)
    app.config['MYSQL_HOST'] = conArgs['mysql']['host']
    app.config['MYSQL_USER'] = conArgs['mysql']['user']
    app.config['MYSQL_PASSWORD'] = conArgs['mysql']['pass']
    app.config['MYSQL_DB'] = conArgs['mysql']['db']

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        print("-------------> ", email)
        print("-------------> ", password)
        if validadMail(email):
            if len(password) > 4:
                cursor.execute('SELECT * FROM accounts WHERE email = % s', (email,))
                account = cursor.fetchone()
                if not account:
                    print()
                    print("password: ", password, len(password))
                    print("email: ", email, len(email))
                    print()
                    cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s)', (email, password,))
                    mysql.connection.commit()
                    msg = 'You have successfully registered !'
                else:
                    msg = 'Account already exists !'
            else:
                msg = 'Password need at least 4 characters'
        else:
            msg = 'Invalid email address !'

    return render_template('register.html', msg=msg)



# validating an Email
def validadMail(email):
    valido = False
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        valido = True

    return valido


if __name__ == "__main__":
    app.run(debug=True)

