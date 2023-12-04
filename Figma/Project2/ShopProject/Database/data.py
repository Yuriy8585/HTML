from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

# Подключаемся к базе данных
conn = sqlite3.connect('visitors.db')
c = conn.cursor()

# Создаем таблицу
c.execute('''CREATE TABLE if not exists visitors
             (id, firstname, lastname, age)''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()




# Подключаемся к базе данных
conn = sqlite3.connect('visitors.db')
c = conn.cursor()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# Вводим данные
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Вставляем данные в таблицу
c.execute("INSERT INTO visitors VALUES (?, ?, ?, ?)", (User))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']
    new_user = User(firstname=firstname, lastname=lastname, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()
