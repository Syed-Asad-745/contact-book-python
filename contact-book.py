import json

class Book:
    def __init__(self):
        self.contacts = {}
        self.read_file()

    def add_contact(self):
        name = input("Enter the name of the contact: ")
        number = input("Enter the number of the contact: ")
        self.contacts[name] = number
        self.save_file()
        print(f"Contact added: '{name}'")

    def update_contact(self):
        name = input("Enter the name of the contact you want to update: ")
        if name in self.contacts:
            number = input("Enter the new Number: ")
            self.contacts[name] = number
            self.save_file()
            print(f"Contact updated: '{name}'")
        else:
            print(f"Contact not found: '{name}'")

    def view_contacts(self):
        if not self.contacts:
            print("Contacts empty!")
        else:
            print("---ALL CONTACTS---")
            for name, number in self.contacts.items():
                print(f"{name} : {number}")

    def search_contact(self):
        name = input("Enter the contact name to search: ")
        if name in self.contacts:
            print(f"\n{name} : {self.contacts[name]}")
        else:
            print(f"\nContact not found: '{name}'")

    def delete_contact(self):
        name = input("Enter the contact name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            self.save_file()
            print(f"\nContact deleted: '{name}'")
        else:
            print(f"\nNo contact found: '{name}'")

    def save_file(self):
        with open("contacts.json", "w") as file:
                json.dump(self.contacts, file, indent = 4)

    def read_file(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = {}

contact_book = Book()

print("*"*10+"Contact Book"+"*"*10)

while True:
    print("-"*32)
    print("Contact Handling Menu")
    print("1. ADD a contact")
    print("2. UPDATE a contact")
    print("3. VIEW all contacts")
    print("4. SEARCH a contact")
    print("5. DELETE a contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        contact_book.add_contact()
    elif choice == "2":
        contact_book.update_contact()
    elif choice == "3":
        contact_book.view_contacts()
    elif choice == "4":
        contact_book.search_contact()
    elif choice == "5":
        contact_book.delete_contact()
    elif choice == "6":
        print("------------------------------------")
        print("Thanks for using the contact book :)")
        print("------------------------------------")
        break
    else:
        print("Please enter a valid choice (1-6)!")
