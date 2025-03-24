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
    result = db_sess.query(Jobs).filter(Jobs.is_finished != 1).all()
    max_len = -200
    for i in range(len(result)):
        if len(result[i].collaboration) > max_len:
            max_len = len(result[i].collaboration)

    for i in range(len(result)):
        if len(result[i].collaboration) == max_len:
            print(result[i].collaboration)



    #app.run()


if __name__ == '__main__':
    main()