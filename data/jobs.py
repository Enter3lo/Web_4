import datetime

import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlALchemyBase


class Jobs(SqlALchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaboration = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # Изменено на String
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    user = orm.relationship('User', back_populates='jobs')  # Удален лишний пробел

    def __repr__(self):
       # return (f"{self.id}, {self.team_leader}, {self.job}, "
        #        f"{self.work_size}, {self.collaboration}, {self.start_date}, "
        #        f"{self.end_date}, {self.is_finished}")
       # запрос 5
        return f"<Job> {self.job} {self.work_size}"