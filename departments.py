import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlALchemyBase

class Department(SqlALchemyBase):
    __tablename__ = 'departments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # Список id's
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relationship('User ', back_populates='departments')

    def __repr__(self):
        return f"<Department> {self.title} {self.chief} {self.email}"
