# Contact Book Program

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\n----- Contact List -----")
        for name, details in contacts.items():
            print(f"Name : {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print("-" * 25)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("\nContact Found:")
        print(f"Name : {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using the Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")