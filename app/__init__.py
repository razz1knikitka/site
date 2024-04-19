from flask import Flask

from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['MAIL_SERVER'] = "sandbox.smtp.mailtrap.io"
app.config['MAIL_PORT'] = "25"
app.config['MAIL_USERNAME'] = "2b5c264c26ebc3"
app.config['MAIL_PASSWORD'] = "eaa7a748843d9b"
app.permanent_session_lifetime = timedelta(minutes=90)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)



@app.route('/mail', methods=['GET'])
def mail_1():
    msg = Message(
        subject='Registration letter',
        sender='noreply@employer.com',
        recipients=['wfe@wef.wef']
    )
    msg.html = 'wef'
    mail.send(msg)


from app import routes
from app import models



if __name__ == '__main__':
    app.run(debug=True)