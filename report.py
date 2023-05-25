from logic import assign_grad_students


def generate_assignment_report(courses, course_directors, grad_students):
    report = "Assignment Report\n\n"

    for course_name, course in courses.items():
        report += f"{course_name}:\n"

        for position in course.positions:
            report += f"\tPosition: {position.name}\n"

            if position.assigned_student:
                report += f"\t\tAssigned Student: {position.assigned_student}\n"
            else:
                report += "\t\tNo student assigned\n"

    return report
