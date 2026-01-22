students = []

def add_student():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    department = input("Enter department: ")

    student = {
        "name": name,
        "matric": matric,
        "department": department
    }

    students.append(student)
    print("Student record added successfully.\n")

def view_students():
    if not students:
        print("No student records available.\n")
        return

    for student in students:
        print("Name:", student["name"])
        print("Matric Number:", student["matric"])
        print("Department:", student["department"])
        print("-----------------------------")

def search_student():
    matric = input("Enter matric number to search: ")
    for student in students:
        if student["matric"] == matric:
            print("Student record found:")
            print("Name:", student["name"])
            print("Matric Number:", student["matric"])
            print("Department:", student["department"])
            return
    print("Student record not found.\n")

def main_menu():
    while True:
        print("Student Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.\n")

main_menu()
