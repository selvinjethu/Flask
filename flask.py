from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="flask_app"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']

    # Insert data into MySQL
    cursor.execute("INSERT INTO users (name, age, city) VALUES (%s, %s, %s)", (name, age, city))
    db.commit()

    return 'Record added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
