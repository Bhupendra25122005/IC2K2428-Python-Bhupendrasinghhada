employees = {
    "E1": {"name": "Shubhman", "dept": "Economics", "salary": 400000},
    "E2": {"name": "Sara", "dept": "Management", "salary": 450000},
    "E3": {"name": "yuzvendra", "dept": "IT", "salary": 75000},
    "E4": {"name": "Dhanashree", "dept": "Finance", "salary": 52000},
    "E5": {"name": "ShoaibAkhtar", "dept": "HR", "salary": 48000}
}


# 1. Add Employee
def add_employee():
    emp_id = input("Enter employee ID: ").strip()

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    dept = input("Enter department: ").strip()
    salary = float(input("Enter salary: "))

    if name == "" or dept == "":
        print("Name and department cannot be empty.")
        return

    if salary < 0:
        print("Salary cannot be negative.")
        return

    employees[emp_id] = {
        "name": name,
        "dept": dept,
        "salary": salary
    }

    print("Employee added successfully!")


# 2. Update Salary
def update_salary():
    emp_id = input("Enter employee ID: ").strip()

    if emp_id not in employees:
        print("Employee not found.")
        return

    salary = float(input("Enter new salary: "))

    if salary < 0:
        print("Salary cannot be negative.")
        return

    employees[emp_id]["salary"] = salary
    print("Salary updated successfully!")


# 3. Delete Employee
def delete_employee():
    emp_id = input("Enter employee ID to delete: ").strip()

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")


# 4. Search Employee by ID
def search_employee():
    emp_id = input("Enter employee ID to search: ").strip()

    if emp_id in employees:
        print("Employee ID:", emp_id)
        print("Name:", employees[emp_id]["name"])
        print("Department:", employees[emp_id]["dept"])
        print("Salary:", employees[emp_id]["salary"])
    else:
        print("Employee not found.")


# 5. Reports
def reports():
    print("\n===== EMPLOYEE REPORTS =====")

    # Department-wise payroll and headcount in one pass
    department_data = {}

    for employee in employees.values():
        dept = employee["dept"]

        if dept not in department_data:
            department_data[dept] = {
                "payroll": 0,
                "headcount": 0
            }

        department_data[dept]["payroll"] += employee["salary"]
        department_data[dept]["headcount"] += 1

    print("\n1. Department-wise Payroll and Headcount:")

    for dept, data in department_data.items():
        print(
            dept,
            "-> Payroll:", data["payroll"],
            "| Headcount:", data["headcount"]
        )

    # Highest-paid employee in each department
    highest_paid = {}

    for emp_id, employee in employees.items():
        dept = employee["dept"]

        if (
            dept not in highest_paid
            or employee["salary"] > highest_paid[dept]["salary"]
        ):
            highest_paid[dept] = {
                "name": employee["name"],
                "salary": employee["salary"]
            }

    print("\n2. Highest-Paid Employee in Each Department:")

    for dept, employee in highest_paid.items():
        print(
            dept, "->", employee["name"],
            "(", employee["salary"], ")"
        )

    # All employees sorted by salary, highest first
    sorted_employees = sorted(
        employees.items(),
        key=lambda item: item[1]["salary"],
        reverse=True
    )

    print("\n3. Employees Sorted by Salary (Highest First):")

    for emp_id, employee in sorted_employees:
        print(
            emp_id, "->", employee["name"],
            "|", employee["dept"],
            "|", employee["salary"]
        )

    # Create a NEW dictionary with a 10% raise for salaries below 50000.
    # We do not modify the original because the question requires the
    # original salaries to remain unchanged for comparison.
    raised_employees = {
        emp_id: {
            **employee,
            "salary": employee["salary"] * 1.10
        }
        if employee["salary"] < 50000
        else employee.copy()
        for emp_id, employee in employees.items()
    }

    print("\n4. New Employee Dictionary After 10% Raise:")

    for emp_id, employee in raised_employees.items():
        print(
            emp_id, "->", employee["name"],
            "| Salary:", employee["salary"]
        )

    print("\nOriginal Salaries (Unchanged):")

    for emp_id, employee in employees.items():
        print(emp_id, "->", employee["name"], employee["salary"])

    # Department with the highest average salary
    department_salary = {}

    for employee in employees.values():
        dept = employee["dept"]

        if dept not in department_salary:
            department_salary[dept] = {
                "total": 0,
                "count": 0
            }

        department_salary[dept]["total"] += employee["salary"]
        department_salary[dept]["count"] += 1

    department_averages = {
        dept: data["total"] / data["count"]
        for dept, data in department_salary.items()
    }

    print("\n5. Department-wise Average Salary:")

    for dept, average in department_averages.items():
        print(dept, "->", round(average, 2))

    if department_averages:
        best_dept = max(department_averages, key=department_averages.get)
        print(
            "\nDepartment with Highest Average Salary:",
            best_dept,
            "->", round(department_averages[best_dept], 2)
        )
    else:
        print("\nNo employees available.")


# Main Menu
while True:
    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search Employee by ID")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_salary()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        reports()
    elif choice == "6":
        print("Exiting Employee Database.")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")