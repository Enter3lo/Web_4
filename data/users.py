import datetime

import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlALchemyBase


class User(SqlALchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    jobs = orm.relationship('Jobs', back_populates='user')
    department = orm.relationship('Department', back_populates='user_department')

    def __repr__(self):
        #Запрос 1
        #return (f"{self.id}, {self.surname}, {self.name}, "
        #        f"{self.age}, {self.position}, {self.speciality}, "
        #        f"{self.address}, {self.email}, "
        #        f"{self.hashed_password}, {self.modified_date}")
        #Запрос 2
        #return f'<colonist> {self.id} {self.surname} {self.name}'
        #Запрос 3
        #return f'<colonist> {self.id} {self.surname} {self.name} {self.age} years'
        #запрос 4
        return f'<colonist> {self.id} {self.surname} {self.name} {self.position}'
