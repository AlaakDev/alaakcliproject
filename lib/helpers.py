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
