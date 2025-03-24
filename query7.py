import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Enter_zlo'


def main():
    # Инициализируем сессию базы данных
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    # Выполняем запрос для изменения адреса колонистов
    colonists = db_sess.query(User).filter(
        User.address.like('%Первый модуль%'),
        User.age < 21
    ).all()
    
    # Изменяем адрес на 'module_3' и сохраняем изменения
    for colonist in colonists:
        colonist.address = 'module_3'
    
    db_sess.commit()  # Сохраняем изменения в базе данных

    # Выводим количество измененных записей
    print(f'Изменено адресов колонистов: {len(colonists)}')

    #app.run()


if __name__ == '__main__':
    main()
