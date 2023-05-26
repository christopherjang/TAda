def generate_assignment_report(courses, assigned_students):
    report = "Assignment Report\n\n"

    for course_name, course in courses.items():
        report += f"{course_name}:\n"

        for position in course.positions:
            report += f"\tPosition: {position.name}\n"
            assigned_students_for_position = [student for student, assigned_position in assigned_students if assigned_position == position]
            if assigned_students_for_position:
                for assigned_student in assigned_students_for_position:
                    report += f"\t\tAssigned Student: {assigned_student}\n"
            else:
                report += "\t\tNo student assigned\n"

    return report
