contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved.")
    elif choice == "2":
        print("\nSaved Contacts:")
        for name in contacts:
            print(f"{name}: {contacts[name]}")
    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"Phone number of {search}: {contacts[search]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice.")
