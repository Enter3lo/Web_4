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

    # Выполняем запрос для получения id колонистов
    colonists = db_sess.query(User).filter(
        User.address.like('%Первый модуль%'),
        ~User .speciality.ilike('%engineer%'),
        ~User .position.ilike('%engineer%')
    ).all()

    # Выводим id колонистов
    for colonist in colonists:
        print(colonist.id)

    #app.run()


if __name__ == '__main__':
    main()
