

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list) and all(isinstance(c, dict) for c in data):
            return data

        print("Warning: Invalid contact data.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not load contacts.")
        return []


def save_contacts(contacts):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)
        return True

    except OSError:
        print("Error: Contacts could not be saved.")
        return False


def add_contact(contacts):
    print("\n========== ADD CONTACT ==========")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    updated_contacts = contacts + [contact]

    if save_contacts(updated_contacts):
        contacts.append(contact)
        print("Contact added successfully!")


def view_contacts(contacts):
    print("\n========== CONTACT LIST ==========")

    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])


def search_contact(contacts):
    search = input("\nEnter name or phone number to search: ").strip().lower()

    if not search:
        print("Search input cannot be empty.")
        return

    found = False

    for contact in contacts:
        if (search in contact["name"].lower() or
                search in contact["phone"].lower()):

            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    if not contacts:
        print("No contacts available to update.")
        return

    view_contacts(contacts)

    try:
        number = int(input("\nEnter contact number to update: "))

        if not 1 <= number <= len(contacts):
            print("Invalid contact number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    updated_contacts = [contact.copy() for contact in contacts]
    contact = updated_contacts[number - 1]

    print("\nEnter new details (press Enter to keep existing value):")

    name = input(f"Name ({contact['name']}): ").strip()
    phone = input(f"Phone ({contact['phone']}): ").strip()
    email = input(f"Email ({contact['email']}): ").strip()
    address = input(f"Address ({contact['address']}): ").strip()

    if name:
        contact["name"] = name

    if phone:
        contact["phone"] = phone

    if email:
        contact["email"] = email

    if address:
        contact["address"] = address

    if save_contacts(updated_contacts):
        contacts[:] = updated_contacts
        print("Contact updated successfully!")


def delete_contact(contacts):
    if not contacts:
        print("No contacts available to delete.")
        return

    view_contacts(contacts)

    try:
        number = int(input("\nEnter contact number to delete: "))

        if not 1 <= number <= len(contacts):
            print("Invalid contact number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    updated_contacts = contacts.copy()
    deleted = updated_contacts.pop(number - 1)

    if save_contacts(updated_contacts):
        contacts[:] = updated_contacts
        print("Contact deleted:", deleted["name"])


def main():
    contacts = load_contacts()

    print("Welcome to Contact Book Application!")

    while True:
        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Contacts are saved. Thank you!")
            break

        else:
            print("Invalid choice! Select between 1 and 6.")


if __name__ == "__main__":
    main()

