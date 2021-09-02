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


def getUsusrios():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM accounts")
    return list(cursor.fetchall())


@app.route('/')
@app.route('/tablabasica', methods=['GET', 'POST'])
def tablabasica():
    usuarios = getUsusrios()
    return render_template('tablabasica.html', title='Tabla Basica', usuarios=usuarios)


@app.route('/tablaajax')
def tablaajax():
    return render_template('tablaajax.html', title='Tabla Ajax')


@app.route('/apidata')
def apidata():
    usuarios = getUsusrios()
    datos = [user for user in usuarios]
    return {'data': datos}


if __name__ == "__main__":
    app.run(debug=True)

