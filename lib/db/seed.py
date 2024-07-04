from faker import Faker
from sqlalchemy.exc import IntegrityError
from models import Person, Phone, Address, session, Base

fake = Faker()

def seed_database(num_entries):
Base.metadata.drop_all(bind=engine) # Drop existing tables (for testing)
Base.metadata.create_all(bind=engine) # Create tables anew

for _ in range(num_entries):
person = Person(name=fake.name())

phone = Phone(number=fake.phone_number(), type='mobile')
person.phones.append(phone)

address = Address(street=fake.street_address(), city=fake.city(), state=fake.state())
person.addresses.append(address)


