# Name of the file used to store all contact records
CONTACTS_FILE = "contacts.txt"


def read_contacts():
    """Read contacts from the file and return a list of dictionaries."""
    contacts = []

    try:
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                fields = line.strip().split(",")

                # A valid contact record contains a name and phone number.
                if len(fields) == 2:
                    name, phone = fields
                    contacts.append({"name": name, "phone": phone})
    except FileNotFoundError:
        # Create an empty contacts file if it does not exist.
        open(CONTACTS_FILE, "w").close()

    return contacts


def write_contacts(contacts):
    """Save the complete contact list back to the original file."""
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")


def is_valid_phone(phone):
    """Check that the phone number contains exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def find_contact(contacts, name):
    """Find a contact by name without considering letter case."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def display_contact(contact):
    """Display one contact in a readable format."""
    print(f"Name: {contact['name']}, Phone Number: {contact['phone']}")


def display_all_contacts():
    """Display every contact stored in contacts.txt."""
    contacts = read_contacts()

    if not contacts:
        print("No contacts found.")
        return

    print("\n--- All Contacts ---")
    for contact in contacts:
        display_contact(contact)


def search_contact():
    """Search for a contact using the person's name."""
    name = input("Enter contact name: ").strip()
    contact = find_contact(read_contacts(), name)

    if contact:
        print("\nContact found:")
        display_contact(contact)
    else:
        print("Contact not found.")


def add_contact():
    """Add a new contact and save it immediately."""
    contacts = read_contacts()
    name = input("Enter contact name: ").strip()

    if not name or "," in name:
        print("Enter a valid name without commas.")
        return

    if find_contact(contacts, name):
        print("A contact with this name already exists.")
        return

    phone = input("Enter 10-digit phone number: ").strip()
    if not is_valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return

    contacts.append({"name": name, "phone": phone})
    write_contacts(contacts)
    print("Contact added successfully.")


def update_contact():
    """Update an existing contact number and save the change."""
    contacts = read_contacts()
    name = input("Enter the contact name to update: ").strip()
    contact = find_contact(contacts, name)

    if not contact:
        print("Contact not found.")
        return

    new_phone = input("Enter the new 10-digit phone number: ").strip()
    if not is_valid_phone(new_phone):
        print("Phone number must contain exactly 10 digits.")
        return

    contact["phone"] = new_phone
    write_contacts(contacts)
    print("Contact number updated successfully.")


def delete_contact():
    """Delete a contact and save the modified contact list."""
    contacts = read_contacts()
    name = input("Enter the contact name to delete: ").strip()
    contact = find_contact(contacts, name)

    if not contact:
        print("Contact not found.")
        return

    contacts.remove(contact)
    write_contacts(contacts)
    print("Contact deleted successfully.")


def display_vowel_contacts():
    """Display contacts whose names begin with a vowel."""
    contacts = read_contacts()

    # lower() allows both uppercase and lowercase names to be checked.
    vowel_contacts = [
        contact
        for contact in contacts
        if contact["name"] and contact["name"][0].lower() in "aeiou"
    ]

    if not vowel_contacts:
        print("No contact names start with a vowel.")
        return

    print("\n--- Contacts Starting With a Vowel ---")
    for contact in vowel_contacts:
        display_contact(contact)


def display_menu():
    """Display all menu options."""
    print("\n===== Mobile Contact Directory System =====")
    print("1. Display all contacts")
    print("2. Search a contact by name")
    print("3. Add a new contact")
    print("4. Update an existing contact number")
    print("5. Delete a contact")
    print("6. Display contacts whose names start with a vowel")
    print("7. Exit")


def main():
    """Run the menu until the user chooses to exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_all_contacts()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            display_vowel_contacts()
        elif choice == "7":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


# Start the application only when this program is run directly.
if __name__ == "__main__":
    main()
