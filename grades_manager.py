def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name:\n").title()
    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n")

        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade.strip())

        subjects[subject] = grade

    student_grades[name] = subjects

    print(f"Student {name} successfully added to the grades management system.")

    return student_grades


def get_students(student_grades, keys):
    result = {}

    # crear mapa en minúsculas para búsqueda case-insensitive
    lower_map = {k.lower(): k for k in student_grades}

    for name in keys:
        key = name.lower()

        if key in lower_map:
            original_name = lower_map[key]
            result[original_name] = student_grades[original_name]
        else:
            print(f"{name.title()} not found!")

    return result


def avg_by_student(student_grades, keys=None):
    # si hay keys → filtrar
    if keys is not None:
        student_grades = get_students(student_grades, keys)

    for student, subjects in student_grades.items():
        if len(subjects) == 0:
            avg = 0
        else:
            avg = sum(subjects.values()) / len(subjects)

        print(f"{student}: {round(avg, 1)}")