def student_averages(students):
    averages = {}

    for student, assignments in students.items():
        if len(assignments) == 0:
            averages[student] = 0
        else:
            total = sum(assignments.values())
            count = len(assignments)
            averages[student] = round(total / count)

    return averages


def assignment_averages(students):
    totals = {}
    counts = {}

    for assignments in students.values():
        for assignment, grade in assignments.items():
            if assignment not in totals:
                totals[assignment] = 0
                counts[assignment] = 0

            totals[assignment] += grade
            counts[assignment] += 1

    averages = {}

    for assignment in totals:
        averages[assignment] = round(totals[assignment] / counts[assignment])

    return averages