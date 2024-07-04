from faker import Faker
from sqlalchemy.exc import IntegrityError
from models import Person, Phone, Address, session, Base, engine

fake = Faker()

def seed_database(num_entries):
    Base.metadata.drop_all(bind=engine)  # Drop existing tables (for testing)
    Base.metadata.create_all(bind=engine)  # Create tables anew

    for _ in range(num_entries):
        person = Person(name=fake.name())

        phone = Phone(number=fake.phone_number(), type='mobile')
        person.phones.append(phone)

        address = Address(street=fake.street_address(), city=fake.city(), state=fake.state())
        person.addresses.append(address)

        session.add(person)

    try:
        session.commit()
        print(f'Successfully seeded database with {num_entries} entries.')
    except IntegrityError as e:
        session.rollback()
        print(f'Error seeding database: {e}')

if __name__ == '__main__':
    seed_database(5)  # Seed database with 5 entries


