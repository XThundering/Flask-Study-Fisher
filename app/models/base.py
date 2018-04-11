"""
 Created by XThundering on 2018/4/10
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

__author__ = 'XThundering'


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
