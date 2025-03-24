from data import db_session
import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from data.fill_departments import fill_departments

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Enter_zlo'

def main():
    db_session.global_init("db/mars_explorer_2.db")
    db_sess = db_session.create_session()
    # Получаем id работников из департамента с id = 1
    department = db_sess.query(Department).filter(Department.id == 1).first()
    if department:
        member_ids = list(map(int, department.members.split(',')))

        # Получаем работников с суммарным количеством отработанных часов больше 25
        results = db_sess.query(User).join(Jobs).filter(
            User.id.in_(member_ids),
            Jobs.work_size > 25
        ).all()
        
        for user in results:
            print(user.surname, user.name)

if __name__ == '__main__':
    main()
