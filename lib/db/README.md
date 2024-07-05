PHONEBOOK CLI APPLICATION

Welcome to the Phonebook CLI Project! This simple command-line interface application allows you to manage a phonebook directly from your terminal. You can add, search, update, and delete contacts easily.

Features
Add new contacts with names and phone numbers
Search for contacts by name
Update existing contact information
Delete contacts
List contacts

Installation
Clone the repository:

Copy code
git clone https://github.com/alaakdev/alaakcliproject.git
cd alaakcliproject
Install the required dependencies:
pip install Click SQLAlchemy Faker

Usage
To run the Phonebook CLI, use the following command:
python lib/cli.py --help

Project Structure

cli.py: This is the main entry point of the CLI application. It defines the commands and their arguments using the click package.

helpers.py: This file contains helper functions that perform the core operations of the phonebook, such

as searching, adding, and deleting persons, as well as adding phone numbers and listing all persons.

db/models.py: This file defines the database models and the database setup using SQLAlchemy.

Follow the on-screen prompts or use the graphical interface to interact with the phonebook.

Commands
Add a contact

add <name> <phone_number>
Example:
add samuel 

Search for a contact
search <name>
Example:
search samuel

Update a contact
update <name> <new_phone_number>
Example:
update samuel

Delete a contact
delete <name>
example;
delete samuel


Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

Contact
If you have any questions or suggestions, feel free to reach out at alaakelijah@gmail.com

Enjoy managing your contacts anytime anywhere with the Phonebook application.