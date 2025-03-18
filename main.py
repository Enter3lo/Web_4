import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Enter_zlo'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = 'Кузнецов'
    user.name = 'Николай'
    user.age = 19
    user.position = 'Диаректор всех директоров'
    user.speciality = 'Директор'
    user.address = 'Город Краторово Левой области Марса Ул. Карл Маркса'
    user.email = 'marsRulit3123@email.com'
    user.hashed_password = '123456788'
    db_sess = db_session.create_session()
    db_sess.add(user)
    capitan = User()
    capitan.surname = 'Скот'
    capitan.name = 'Ридлер'
    capitan.age = 21
    capitan.position = 'Капитан'
    capitan.speciality = 'Инженер'
    capitan.address = 'Первый модуль'
    email = 'marsR3123@email.com'
    user.hashed_password = '123456788'
    db_sess.add(capitan)
    db_sess.commit()
    for user in db_sess.query(User).all():
        print(user)
    work = Jobs()
    work.team_leader = db_sess.query(User.id).filter(User.position == 'Капитан').first()[0]
    work.job = 'Работаю за гроши и всем доволен'
    work.work_size = 8
    work.collaboration = '1, 2, 5'
    end_date_str = '30.04.2025'
    work.end_date = datetime.datetime.strptime(end_date_str, '%d.%m.%Y')
    work.is_finished = False
    db_sess.add(work)
    db_sess.commit()
    for work in db_sess.query(Jobs).all():
        print(work)
    #app.run()


if __name__ == '__main__':
    main()