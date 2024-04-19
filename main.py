import flask
from flask import Flask, request, jsonify, render_template, redirect
from flask_mail import Mail, Message
import sqlite3
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from app.models import City

app = Flask(__name__)

con = sqlite3.connect('instance/db.db')

oon = con.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/db_set')
def show_template():
    if not City.query.all():
        city = City(name='paris', description='good sity', img='http://127.0.0.1:5000/static/img/img-1.jpg')
        city = City(name='new york', description='so good sity', img='http://127.0.0.1:5000/static/img/img-2.jpg')
        city = City(name='london', description='so so good sity', img='http://127.0.0.1:5000/static/img/img-3.jpg')
        city = City(name='amsterdam', description='SO SO SO GOOD SITY', img='http://127.0.0.1:5000/static/img/img-4.jpg')
        city = City(name='australia', description='good sity', img='http://127.0.0.1:5000/static/img/img-5.jpg')
        city = City(name='japan', description='good sity', img='http://127.0.0.1:5000/static/img/img-6.jpg')
        db.session.add(city)
        db.session.commit()
        return 'cities was created'

    return 'cities exist'


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/lst')
def cont():
    return render_template('contact.html')

@app.route('/listing')
def listing():
    return render_template('listing.html')


@app.route('/newyork')
def new():
    return render_template('newyork.html')

@app.route('/paris')
def par():
    return render_template('paris.html')

@app.route('/london')
def lon():
    return render_template('london.html')

@app.route('/amst')
def ams():
    return render_template('amst.html')

@app.route('/ast')
def ast():
    return render_template('ast.html')

@app.route('/jup')
def jup():
    return render_template('jup.html')

@app.route('/contactus', methods=['POST'])
def contact_us():
    if request.method == 'POST':
        email = request.form['mail']
        name = request.form['name']
        txt = request.form['textarea']

        msg = Message(
            subject='Contact letter',
            sender='noreply@employer.com',
            recipients=[email]
        )
        msg.html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <h3>Dear, {name}</h3>
                <h5>thx for contacting us</h5>
            </body>
            </html>
        """
        mail.send(msg)

        return redirect('/lst')

















if __name__ == '__main__':
    app.run(debug=True)
