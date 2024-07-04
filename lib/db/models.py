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
    __tablename__ = 'phone'
id = Column(Integer, primary_key=True)
number = Column(String)
type = Column(String)
person_id = Column(Integer, ForeignKey('person.id'))

person = relationship('Person', back_populates='phones')

def __repr__(self):
return f'<Phone(id={self.id}, number={self.number}, type={self.type})>'

class Address(Base):
__tablename__ = 'address'
id = Column(Integer, primary_key=True)
street = Column(String)
city = Column(String)
state = Column(String)
person_id = Column(Integer, ForeignKey('person.id'))

person = relationship('Person', back_populates='addresses')

def __repr__(self):
return f'<Address(id={self.id}, street={self.street}, city={self.city}, state={self.state})>'

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
