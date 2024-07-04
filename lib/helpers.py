from db.models import session, Person, Phone

def search_person_by_name(name):
    persons = session.query(Person).filter(Person.name.ilike(f'%{name}%')).all()
    if persons:
        for person in persons:
            print(f"Person: {person.name}")
            print("Phones:")
            for phone in person.phones:
                print(f" - {phone.number} ({phone.type})")
            print("Addresses:")
            for address in person.addresses:
                print(f" - {address.street}, {address.city}, {address.state}")
    else:
        print(f"No person found with name '{name}'.")

def add_new_person(name):
    person = Person(name=name)
    session.add(person)
    session.commit()
    print(f"Added new person '{name}' to the phonebook.")

def add_phone_to_person(person_id, number, phone_type):
    person = session.query(Person).filter_by(id=person_id).first()
    if person:
        phone = Phone(number=number, type=phone_type)
        person.phones.append(phone)
        session.commit()
        print(f"Added phone number '{number}' ({phone_type}) to person '{person.name}'.")
    else:
        print(f"Person with ID '{person_id}' not found.")

