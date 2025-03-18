import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Enter_zlo'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    for user in db_sess.query(User).all():
      print(user)

    #app.run()


if __name__ == '__main__':
    main()