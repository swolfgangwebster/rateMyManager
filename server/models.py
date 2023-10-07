from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from config import db

# Models go here!

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    screenname = Column(String())
    password = Column(String())
    review = relationship('Review', backref='user')

class Manager(Base):
    __tablename__ = 'managers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    workplace = Column(String())
    review = relationship("Review", backref='manager')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    p1 = Column(Integer())
    p2 = Column(Integer())
    p3 = Column(Integer())
    manager_id = Column(Integer(), ForeignKey('managers.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
    workplace_id = Column(Integer(), ForeignKey('workplaces.id'))

class Workplace(Base):
    __tablename__ = 'workplaces'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    review = relationship("Review", backref='workplace')

class Workplace_manager(Base):
    __tablename__ = 'workplace_managers'

    id = Column(Integer(), primary_key=True)
    workplace_id = Column(ForeignKey('workplaces.id'))
    manager_id = Column(ForeignKey('managers.id'))

    workplace = relationship('Workplace', back_populates='workplace_managers')
    manager = relationship('Manager', back_populates='workplace_managers')