from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/contactus')
def cont():
    return render_template('contact.html')

@app.route('/listing')
def listing():
    return render_template('listing.html')













if __name__ == '__main__':
    app.run(debug=True)
