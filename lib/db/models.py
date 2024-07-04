from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///phonebook.db', echo=False)
Base = declarative_base()

class Person(Base):
__tablename__ = 'person'
id = Column(Integer, primary_key=True)
name = Column(String)

phones = relationship('Phone', back_populates='person')
addresses = relationship('Address', back_populates='person')

def __repr__(self):
return f'<Person(id={self.id}, name={self.name})>'

class Phone(Base):
