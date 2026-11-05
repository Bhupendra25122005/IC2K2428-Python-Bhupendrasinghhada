
# Q3. Library Record System using Dictionaries

books = {
    "B1": {
        "title": "Python Basics",
        "author": "Bhupendra",
        "copies": 8,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "RohitSharma",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "BhagwadGeeta",
        "author": "Maharishi Ved Vyasa)",
        "copies": 1,
        "issued_to": []
    }
}


# Add Book
def add_book():
    isbn = input("Enter ISBN: ").strip()

    if isbn in books:
        copies = int(input("Enter additional copies: "))

        if copies <= 0:
            print("Copies must be greater than zero.")
            return

        books[isbn]["copies"] += copies
        print("Copies added successfully!")
        return

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    copies = int(input("Enter number of copies: "))

    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return

    if copies <= 0:
        print("Copies must be greater than zero.")
        return

    books[isbn] = {
        "title": title,
        "author": author,
        "copies": copies,
        "issued_to": []
    }

    print("Book added successfully!")


# Issue Book
def issue_book():
    isbn = input("Enter ISBN: ").strip()
    member = input("Enter member ID: ").strip()

    if isbn not in books:
        print("Book not found.")
        return

    if member == "":
        print("Member ID cannot be empty.")
        return

    book = books[isbn]

    if member in book["issued_to"]:
        print("Rejected: Member already holds this book.")
        return

    # Build the current member-to-books mapping
    member_books = {}

    for book_id, record in books.items():
        for member_id in record["issued_to"]:
            member_books.setdefault(member_id, []).append(book_id)

    if len(member_books.get(member, [])) >= 2:
        print("Rejected: Member already holds 2 books.")
        return

    if book["copies"] <= 0:
        print("Rejected: No copies left.")
        return

    book["copies"] -= 1
    book["issued_to"].append(member)

    print("Book issued successfully!")
    print("Remaining copies:", book["copies"])


# Return Book
def return_book():
    isbn = input("Enter ISBN: ").strip()
    member = input("Enter member ID: ").strip()

    if isbn not in books:
        print("Book not found.")
        return

    if member not in books[isbn]["issued_to"]:
        print("Rejected: Member does not hold this book.")
        return

    books[isbn]["issued_to"].remove(member)
    books[isbn]["copies"] += 1

    print("Book returned successfully!")
    print("Available copies:", books[isbn]["copies"])


# Search Book
def search_book():
    print("\n1. Search by ISBN")
    print("2. Search by title")
    print("3. Search by author")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        isbn = input("Enter ISBN: ").strip()

        if isbn in books:
            print(isbn, "->", books[isbn])
        else:
            print("Book not found.")

    elif choice == "2":
        title = input("Enter title: ").strip().lower()

        results = {
            isbn: book
            for isbn, book in books.items()
            if title in book["title"].lower()
        }

        if results:
            print(results)
        else:
            print("No matching books found.")

    elif choice == "3":
        author = input("Enter author name: ").strip().lower()

        results = {
            isbn: book
            for isbn, book in books.items()
            if author in book["author"].lower()
        }

        if results:
            print(results)
        else:
            print("No matching books found.")

    else:
        print("Invalid search choice.")


# Reports
def reports():
    print("\n===== LIBRARY REPORTS =====")

    # 1. Books by a given author (case-insensitive)
    author = input("Enter author name: ").strip().lower()

    author_books = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["author"].lower() == author
    }

    print("\n1. Books by", author.title(), ":")
    print(author_books if author_books else "No books found.")

    # 2. Invert data to build member -> list of books
    member_books = {}

    for isbn, book in books.items():
        for member in book["issued_to"]:
            member_books.setdefault(member, []).append(isbn)

    multiple_books = {
        member: issued_books
        for member, issued_books in member_books.items()
        if len(issued_books) > 1
    }

    print("\n2. Members Holding More Than One Book:")
    print(multiple_books if multiple_books else "None")

    # 3. Books currently unavailable
    unavailable = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["copies"] == 0
    }

    print("\n3. Books Currently Unavailable:")
    print(unavailable if unavailable else "None")

    # 4. Books that have never been issued
    never_issued = {
        isbn: book["title"]
        for isbn, book in books.items()
        if len(book["issued_to"]) == 0
        and book["copies"] >= 0
        and not book.get("ever_issued", False)
    }

    print("\n4. Books Never Issued:")
    print(never_issued if never_issued else "None")


# Main Menu
while True:
    print("\n===== LIBRARY RECORD SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        reports()
    elif choice == "6":
        print("Exiting Library Record System.")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")