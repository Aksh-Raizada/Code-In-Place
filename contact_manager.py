# Constants for file operations
CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """
    Loads contacts from the CONTACTS_FILE.
    Each contact is expected to be on a new line with Name,Phone,Email.
    Returns a list of dictionaries, where each dictionary represents a contact.
    """
    contacts = []
    try:
        with open(CONTACTS_FILE, 'r') as file_reader:
            for line in file_reader.readlines():
                cleaned_line = line.strip()
                if cleaned_line: # Ensure line is not empty
                    parts = cleaned_line.split(',')
                    if len(parts) == 3: # Expecting Name, Phone, Email
                        contact = {
                            'name': parts[0].strip(),
                            'phone': parts[1].strip(),
                            'email': parts[2].strip()
                        }
                        contacts.append(contact)
                    else:
                        print(f"Skipping malformed line in {CONTACTS_FILE}: {cleaned_line}")
    except FileNotFoundError:
        print(f"'{CONTACTS_FILE}' not found. Starting with an empty contact list.")
    return contacts

def save_contacts(contacts):
    """
    Saves the list of contacts to the CONTACTS_FILE.
    Each contact is written as a comma-separated string on a new line.
    """
    try:
        with open(CONTACTS_FILE, 'w') as file_writer:
            for contact in contacts:
                file_writer.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
        print("Contacts saved successfully!")
    except IOError as e:
        print(f"Error saving contacts: {e}")

def add_contact(contacts):
    """
    Prompts the user for contact details and adds a new contact to the list.
    """
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()

    if name and phone and email: # Simple validation that fields are not empty
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        contacts.append(new_contact)
        print(f"Contact '{name}' added.")
    else:
        print("All fields (name, phone, email) must be filled. Contact not added.")

def view_contacts(contacts):
    """
    Displays all contacts currently in the list.
    """
    print("\n--- Your Contacts ---")
    if not contacts:
        print("No contacts found. Add some contacts first!")
        return

    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print("-" * 25) # Separator for readability

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- Contact Manager Menu ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Save Contacts")
    print("4. Load Contacts")
    print("5. Exit")
    print("----------------------------")

def main():
    """
    Main function to run the Contact Manager application.
    """
    contacts = [] # Initialize an empty list to store contacts

    # Optionally load contacts at startup
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
            # After adding, you might want to auto-save or prompt to save
            # save_contacts(contacts) # Uncomment to auto-save after add
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            save_contacts(contacts)
        elif choice == '4':
            contacts = load_contacts() # Overwrite current list with loaded contacts
            print("Contacts reloaded from file.")
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            save_contacts(contacts) # Save before exiting as a good practice
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == '__main__':
    main()
