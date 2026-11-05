
# Q5. Phone Directory using Dictionaries and Lists

contacts = {
    "Anita": {
        "phones": ["7843543210"],
        "email": "Kohli@mail.com",
        "city": "London"
    },
    "Manoj": {
        "phones": ["9900456780", "9876544321"],
        "email": "vivrechard@mail.com",
        "city": "Delhi"
    },
    "Zara": {
        "phones": ["9435678901"],
        "email": "brettlee@mail.com",
        "city": "southafrica"
    }
}


# Validate phone number
def valid_phone(number):
    return len(number) == 10 and number.isdigit()


# Check whether a number belongs to another contact
def number_owner(number):
    for name, details in contacts.items():
        if number in details["phones"]:
            return name
    return None


# 1. Add Contact
def add_contact():
    name = input("Enter contact name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    number = input("Enter 10-digit phone number: ").strip()

    if not valid_phone(number):
        print("Rejected: Phone number must contain exactly 10 digits.")
        return

    owner = number_owner(number)

    if owner is not None:
        print("Rejected: Number already belongs to", owner)
        return

    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()

    contacts[name] = {
        "phones": [number],
        "email": email,
        "city": city
    }

    print("Contact added successfully!")


# 2. Add Another Number
def add_number():
    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    number = input("Enter additional phone number: ").strip()

    if not valid_phone(number):
        print("Rejected: Phone number must contain exactly 10 digits.")
        return

    owner = number_owner(number)

    if owner is not None:
        print("Rejected: Number already belongs to", owner)
        return

    contacts[name]["phones"].append(number)
    print("Phone number added successfully!")


# 3. Update Email or City
def update_contact():
    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update Email")
    print("2. Update City")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        email = input("Enter new email: ").strip()
        contacts[name]["email"] = email
        print("Email updated successfully!")

    elif choice == "2":
        city = input("Enter new city: ").strip()
        contacts[name]["city"] = city
        print("City updated successfully!")

    else:
        print("Invalid choice.")


# 4. Delete Contact
def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# 5. Search
def search_contact():
    print("\n1. Search by Partial Name")
    print("2. Reverse Lookup by Phone Number")
    print("3. Search by Exact Name")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        part = input("Enter part of the name: ").strip().lower()

        results = {
            name: details
            for name, details in contacts.items()
            if part in name.lower()
        }

        if results:
            for name, details in sorted(results.items()):
                print(name, "->", details)
        else:
            print("No matching contacts found.")

    elif choice == "2":
        number = input("Enter phone number: ").strip()

        # Build a number -> name dictionary using comprehension
        phone_directory = {
            phone: name
            for name, details in contacts.items()
            for phone in details["phones"]
        }

        if number in phone_directory:
            print("Number belongs to:", phone_directory[number])
        else:
            print("Phone number not found.")

    elif choice == "3":
        name = input("Enter exact name: ").strip()

        if name in contacts:
            print(name, "->", contacts[name])
        else:
            print("Contact not found.")

    else:
        print("Invalid search choice.")


# 6. Reports
def reports():
    print("\n===== PHONE DIRECTORY REPORTS =====")

    # Group contacts by city
    city_groups = {}

    for name, details in contacts.items():
        city = details["city"]
        city_groups.setdefault(city, []).append(name)

    city_groups = {
        city: sorted(names)
        for city, names in sorted(city_groups.items())
    }

    print("\n1. Contacts Grouped by City:")
    print(city_groups)

    # Contacts having more than one phone number
    multiple_numbers = {
        name: details["phones"]
        for name, details in contacts.items()
        if len(details["phones"]) > 1
    }

    print("\n2. Contacts with More Than One Number:")
    print(multiple_numbers if multiple_numbers else "None")

    # Print complete directory alphabetically
    print("\n3. Complete Directory (Alphabetical):")

    for name, details in sorted(contacts.items()):
        print("Name:", name)
        print("Phone Numbers:", ", ".join(details["phones"]))
        print("Email:", details["email"])
        print("City:", details["city"])
        print("-" * 30)


# Main Menu
while True:
    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        add_number()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        reports()
    elif choice == "7":
        print("Exiting Phone Directory.")
        break
    else:
        print("Invalid choice! Please select between 1 and 7.")