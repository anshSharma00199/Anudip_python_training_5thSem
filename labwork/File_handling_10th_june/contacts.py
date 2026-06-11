# Mobile Contact Directory System

def read_contacts():
    contacts = []
    file = open("contacts.txt", "r")
    for line in file:
        data = line.strip().split(",")
        contacts.append(data)
    file.close()
    return contacts


def write_contacts(contacts):
    file = open("contacts.txt", "w")
    for contact in contacts:
        file.write(contact[0] + "," + contact[1] + "\n")
    file.close()


def display_contacts():
    contacts = read_contacts()

    print("\nContact List")
    print("------------------")
    for contact in contacts:
        print("Name:", contact[0], "Number:", contact[1])


def search_contact():
    contacts = read_contacts()
    name = input("Enter Name: ")

    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Name:", contact[0])
            print("Number:", contact[1])
            return

    print("Contact Not Found")


def add_contact():
    contacts = read_contacts()

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    contacts.append([name, number])

    write_contacts(contacts)

    print("Contact Added Successfully")


def update_contact():
    contacts = read_contacts()

    name = input("Enter Name to Update: ")

    for contact in contacts:
        if contact[0].lower() == name.lower():
            new_number = input("Enter New Number: ")
            contact[1] = new_number
            write_contacts(contacts)
            print("Contact Updated")
            return

    print("Contact Not Found")


def delete_contact():
    contacts = read_contacts()

    name = input("Enter Name to Delete: ")

    for contact in contacts:
        if contact[0].lower() == name.lower():
            contacts.remove(contact)
            write_contacts(contacts)
            print("Contact Deleted")
            return

    print("Contact Not Found")


def vowel_contacts():
    contacts = read_contacts()

    print("\nContacts Starting with Vowel")
    vowels = "AEIOUaeiou"

    for contact in contacts:
        if contact[0][0] in vowels:
            print(contact[0], contact[1])


while True:
    print("\n===== Mobile Contact Directory System =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Display Contacts Starting with Vowel")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        vowel_contacts()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")