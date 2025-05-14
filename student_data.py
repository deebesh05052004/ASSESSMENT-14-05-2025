students = []

def add(student):
    students.append(student)

def get_all():
    return students

def find_by_id(student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None

def update(student_id, new_data):
    for student in students:
        if student["id"] == student_id:
            student.update(new_data)
            return True
    return False

def delete(student_id):
    global students
    original_len = len(students)
    students = [s for s in students if s["id"] != student_id]
    return len(students) < original_len

def find_by_name(name):
    return [s for s in students if s["name"].lower() == name.lower()]

def count():
    return len(students)

def find_by_grade(grade):
    return [s for s in students if s["grade"].lower() == grade.lower()]
