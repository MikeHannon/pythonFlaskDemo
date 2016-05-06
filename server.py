from flask import Flask, render_template, request, redirect, session, flash
from connection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

#to generate

#to check returns boolean:
# bcrypt.check_password_hash(hashed_pw, pw_attempt)
app = Flask(__name__)
bcrypt = Bcrypt(app)
db = MySQLConnector(app, 'mydb')
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    hashed_pw = bcrypt.generate_password_hash("password")
    print hashed_pw
    query = "SELECT * FROM users"
    print "Query"
    print "*"*50
    print query
    print "*"*50
    print (db.query_db(query))
    return render_template('index.html')

@app.route('/register', methods = ['post'])
def somemethod():
    print request.form # immutable dictionary
    query = "INSERT into users (first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :password, NOW(), NOW())"

    values = {  "first_name":request.form['first_name'],
                "last_name":request.form['last_name'],
                "email":request.form['email'],
                "password":request.form['password'],
             }

    print "*"*50
    print query
    print "*"*50
    db.query_db(query,values)
    return render_template('index.html')



if __name__ == '__main__':
  app.run(debug = True)
