def assignment_averages(students):
    result = {}

    if not students:
        return result

    first_student = list(students.values())[0]

    for assignment in first_student:
        total = 0
        count = 0

        for grades in students.values():
            total += grades[assignment]
            count += 1

        result[assignment] = round(total / count)

    return result