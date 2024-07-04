from helpers import search_person_by_name, add_new_person, add_phone_to_person, delete_person_by_id
import sys

if __name__ == '__main__':
    print('Welcome to Phonebook CLI!')

    while True:
        print('\nMenu:')
        print('1. Search for a person by name')
        print('2. Add a new person to the phonebook')
        print('3. Add a phone number to an existing person')
        print('4. Delete a person from the phonebook')
        print('5. Exit\n')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter the name to search: ')
            search_person_by_name(name)
        elif choice == '2':
            name = input('Enter the name of the new person: ')
            add_new_person(name)
        elif choice == '3':
            person_id = input('Enter the ID of the person: ')
            number = input('Enter the phone number: ')
            phone_type = input('Enter the type of phone number: ')
            add_phone_to_person(person_id, number, phone_type)
        elif choice == '4':
            person_id = input('Enter the ID of the person to delete: ')
            delete_person_by_id(person_id)
        elif choice == '5':
            print('Exiting Phonebook CLI.')
            break
        else:
            print('Invalid choice. Please try again.')
