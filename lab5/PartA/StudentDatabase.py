students = {
    101: {
        "name": "Viratkohli",
        "marks": {"Math": 88, "Physics": 76, "Chem": 92}
    },
    102: {
        "name": "RohitSharma",
        "marks": {"Math": 35, "Physics": 58, "Chem": 64}
    },
    103: {
        "name": "MSDhoni",
        "marks": {"Math": 72, "Physics": 81, "Chem": 69}
    }
}


# Function to input valid marks
def get_marks():
    marks = int(input("Enter marks (0-100): "))

    while marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        marks = int(input("Enter marks (0-100): "))

    return marks


# 1. Add a student
def add_student():
    roll_no = int(input("Enter roll number: "))

    if roll_no in students:
        print("Duplicate roll number! Student not added.")
        return

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    n = int(input("Enter number of subjects: "))

    if n <= 0:
        print("Number of subjects must be positive.")
        return

    marks = {}

    for i in range(n):
        subject = input("Enter subject name: ").strip()

        if subject == "":
            print("Subject name cannot be empty.")
            continue

        if subject in marks:
            print("Subject already entered. Try another subject.")
            continue

        marks[subject] = get_marks()

    students[roll_no] = {"name": name, "marks": marks}
    print("Student added successfully!")


# 2. Update subject marks
def update_marks():
    roll_no = int(input("Enter roll number: "))

    if roll_no not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ").strip()

    if subject == "":
        print("Subject name cannot be empty.")
        return

    marks = get_marks()
    students[roll_no]["marks"][subject] = marks

    print("Marks added/updated successfully!")


# 3. Delete a student
def delete_student():
    roll_no = int(input("Enter roll number to delete: "))

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# 4. Show a student's full record
def show_record():
    roll_no = int(input("Enter roll number: "))

    if roll_no not in students:
        print("Student not found.")
        return

    student = students[roll_no]

    print("\nRoll Number:", roll_no)
    print("Name:", student["name"])
    print("Marks:", student["marks"])

    if student["marks"]:
        average = sum(student["marks"].values()) / len(student["marks"])
        print("Average:", round(average, 2))
    else:
        print("Average: No marks available")


# 5. Generate reports
def reports():
    averages = {
        roll: round(sum(s["marks"].values()) / len(s["marks"]), 2)
        for roll, s in students.items()
        if s["marks"]
    }

    print("\n--- STUDENT REPORTS ---")

    # Average marks
    print("\n1. Average Marks:")
    for roll, average in averages.items():
        print(roll, "->", students[roll]["name"], ":", average)

    # Topper
    if averages:
        topper = max(averages, key=averages.get)
        print("\n2. Topper:", students[topper]["name"])
    else:
        print("\n2. Topper: No students with marks.")

    # Highest scorer in each subject
    subject_scores = {}

    for student in students.values():
        for subject, score in student["marks"].items():
            subject_scores.setdefault(subject, []).append(
                (score, student["name"])
            )

    print("\n3. Highest Scorer in Each Subject:")

    for subject, scores in subject_scores.items():
        highest = max(score for score, name in scores)
        names = [
            name for score, name in scores if score == highest
        ]
        print(subject, "->", ", ".join(names), "(", highest, ")")

    # Students scoring below 40
    below_40 = {
        s["name"]: {
            subject: score
            for subject, score in s["marks"].items()
            if score < 40
        }
        for s in students.values()
        if any(score < 40 for score in s["marks"].values())
    }

    print("\n4. Students Scoring Below 40:")

    if below_40:
        for name, subjects in below_40.items():
            print(name, "->", subjects)
    else:
        print("No students scored below 40.")

    # Grade-wise grouping based on average marks
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for roll, average in averages.items():
        if average >= 90:
            grades["A"].append(students[roll]["name"])
        elif average >= 75:
            grades["B"].append(students[roll]["name"])
        elif average >= 60:
            grades["C"].append(students[roll]["name"])
        elif average >= 40:
            grades["D"].append(students[roll]["name"])
        else:
            grades["F"].append(students[roll]["name"])

    print("\n5. Grade-wise Grouping:")
    print(grades)


# Main menu
while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Add a student")
    print("2. Update subject marks")
    print("3. Delete a student")
    print("4. Show student record")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_record()
    elif choice == "5":
        reports()
    elif choice == "6":
        print("Exiting Student Database.")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")