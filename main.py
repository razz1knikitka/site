from app import config
from datetime import timedelta
from flask import Flask, request, render_template, redirect
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

# todo: refactor codebase so you can get rid of app module. (done)
# todo: get rid of app module
app = Flask(__name__)
app.config.from_object(config.Config)
app.config['MAIL_SERVER'] = "sandbox.smtp.mailtrap.io" # todo: move to env or config file
app.config['MAIL_PORT'] = "25" # todo: move to env or config file
app.config['MAIL_USERNAME'] = "2b5c264c26ebc3" # todo: move to env or config file
app.config['MAIL_PASSWORD'] = "eaa7a748843d9b" # todo: move to env or config file
app.permanent_session_lifetime = timedelta(minutes=90)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = Column(db.String)
    img = Column(db.String)

@app.route('/db_set')
def show_template():
    if not City.query.all():
        cities = []

        cities.append(City(name='paris', description='good sity', img='http://127.0.0.1:5000/static/img/img-1.jpg'))
        cities.append(City(name='new york', description='so good sity', img='http://127.0.0.1:5000/static/img/img-2.jpg'))
        cities.append(City(name='london', description='so so good sity', img='http://127.0.0.1:5000/static/img/img-3.jpg'))
        cities.append(City(name='amsterdam', description='SO SO SO GOOD SITY', img='http://127.0.0.1:5000/static/img/img-4.jpg'))
        cities.append(City(name='australia', description='good sity', img='http://127.0.0.1:5000/static/img/img-5.jpg'))
        cities.append(City(name='japan', description='good sity', img='http://127.0.0.1:5000/static/img/img-6.jpg'))
        for city in cities:
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

# todo: example
# @app.route('/<city_name>')
# def par(city_name):
#     city = City.query.filter(name=city_name).first()
#
#     if not city:
#         return str(f'City `{city_name}` Not Found'), 404
#
#     return render_template('paris.html', city=city)

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
        txt = request.form['textarea']  # todo: remove unused code

        msg = Message(
            subject='Contact letter',
            sender='noreply@employer.com',  # todo: set ur domain name (extra  todo: get domain using Flask)
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
