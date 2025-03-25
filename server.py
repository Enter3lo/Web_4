from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import render_template, Flask, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def main():
    return render_template('main.html')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


