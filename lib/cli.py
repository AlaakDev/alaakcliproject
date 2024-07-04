from helpers import search_person_by_name, add_new_person, add_phone_to_person
import sys

if __name__ == '__main__':
print('Welcome to Phonebook CLI!')

while True:
print('\nMenu:')
print('1. Search for a person by name')
print('2. Add a new person to the phonebook')
print('3. Add a phone number to an existing person')
print('4. Exit\n')

choice = input('Enter your choice: ')
