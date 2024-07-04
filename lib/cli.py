import click
from helpers import search_person_by_name, add_new_person, add_phone_to_person, delete_person_by_id, list_all_persons

@click.group()
def cli():
    """Welcome to Phonebook CLI!"""
    pass

@cli.command()
@click.argument('name')
def search(name):
    """Search for a person by name"""
    search_person_by_name(name)

@cli.command()
@click.argument('name')
def add(name):
    """Add a new person to the phonebook"""
    add_new_person(name)

@cli.command()
@click.argument('person_id')
@click.argument('number')
@click.argument('phone_type')
def add_phone(person_id, number, phone_type):
    """Add a phone number to an existing person"""
    add_phone_to_person(person_id, number, phone_type)

@cli.command()
@click.argument('person_id')
def delete(person_id):
    """Delete a person from the phonebook"""
    delete_person_by_id(person_id)

@cli.command()
def list_all():
    """List all persons in the phonebook"""
    list_all_persons()

if __name__ == '__main__':
    cli()


