# Employee database using a dictionary
employees = {
    1001: {'name': 'Alok', 'age': 29, 'department': 'Operation', 'salary': 60000},
    1002: {'name': 'Bony', 'age': 26, 'department': 'Supply', 'salary': 50000},
    1003: {'name': 'Camelia', 'age': 28, 'department': 'HR', 'salary': 70000}
}

def display_employee(emp_id):
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Salary     : {emp['salary']}")
    else:
        print("Employee not found.")

def add_employee():
    try:
        emp_id = int(input("Enter New Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists.")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        employees[emp_id] = {'name': name, 'age': age, 'salary': salary}
        print("Employee added successfully.")
    except ValueError:
        print("Invalid input! Please enter proper .")

def search_employee():
    print(employees)

# Menu loop
while True:
    print("===== Employee Menu =====")
    print("1. Search Employee Details")
    print("2. Add New Employee")
    print("3. View all employees")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        try:
            emp_id = int(input("Enter Employee ID: "))
            display_employee(emp_id)
        except ValueError:
            print("Invalid input! Please enter a valid numeric ID.\n")
    elif choice == '2':
        add_employee()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        print("Exiting the program. Thank You!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.\n")