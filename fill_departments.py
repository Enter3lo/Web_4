from data import db_session
from departments import Department

def fill_departments():
    db_sess = db_session.create_session()
    
    # Пример заполнения
    department1 = Department(title='Геологическая разведка', chief=1, members='1, 2, 3', email='geo@mars.com')
    department2 = Department(title='Инженерный отдел', chief=2, members='4, 5', email='eng@mars.com')
    
    db_sess.add(department1)
    db_sess.add(department2)
    db_sess.commit()
