def student_averages(students):
    result = {}
    
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)
    
    return result


def assignment_averages(students):
    result = {}
    
    # Obtener nombres de tareas (del primer estudiante)
    assignments = next(iter(students.values())).keys()
    
    for assignment in assignments:
        total = 0
        count = 0
        
        for grades in students.values():
            total += grades[assignment]
            count += 1
        
        avg = total / count
        result[assignment] = round(avg)
    
    return result