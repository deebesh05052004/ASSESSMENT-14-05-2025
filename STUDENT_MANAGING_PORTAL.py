import JSON

def add_student():
    try:
        student = {
            "id": int(input("Enter student ID: ")),
            "name": input("Enter student name: "),
            "age": int(input("Enter student age: ")),
            "grade": input("Enter student grade: ")
        }
        if student_data.find_by_id(student["id"]):
            print("Student ID already exists.")
        else:
            student_data.add(student)
            print("Student added.")
    except ValueError:
        print("Invalid input.")

def list_students():
    students = student_data.get_all()
    if not students:
        print("No students found.")
    for student in students:
        print(student)

def get_student_by_id():
    try:
        student_id = int(input("Enter student ID to find: "))
        student = student_data.find_by_id(student_id)
        print(student if student else "Student not found.")
    except ValueError:
        print("Invalid ID.")

def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        new_data = {}
        age = input("Enter new age (or press enter to skip): ")
        grade = input("Enter new grade (or press enter to skip): ")
        if age:
            new_data["age"] = int(age)
        if grade:
            new_data["grade"] = grade
        if student_data.update(student_id, new_data):
            print("Student updated.")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input.")

def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        if student_data.delete(student_id):
            print("Student deleted.")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid ID.")

def search_student_by_name():
    name = input("Enter name to search: ").lower()
    results = student_data.find_by_name(name)
    if results:
        for student in results:
            print(student)
    else:
        print("No matching student found.")

def count_students():
    print(f"Total students: {student_data.count()}")

def get_students_by_grade():
    grade = input("Enter grade to filter by: ").lower()
    results = student_data.find_by_grade(grade)
    if results:
        for student in results:
            print(student)
    else:
        print("No students in that grade.")

def main():
    while True:
        print("\n===== Student Manager Menu =====")
        print("1. Add Student")
        print("2. List All Students")
        print("3. Find Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Search Student by Name")
        print("7. Count Total Students")
        print("8. List Students by Grade")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            get_student_by_id()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            search_student_by_name()
        elif choice == "7":
            count_students()
        elif choice == "8":
            get_students_by_grade()
        elif choice == "9":
            print("Exiting Student Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 9.")

if __name__ == "__main__":
    main()
