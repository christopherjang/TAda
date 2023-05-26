import csv


def generate_assignment_report(courses, assigned_students, output_file):
    report = "Assignment Report\n\n"

    # Save data to CSV
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Course', 'Student', 'Position'])

        for course_name, course in courses.items():
            for position in course.positions:
                assigned_students_for_position = [(student, assigned_position) for student, assigned_position in
                                                  assigned_students if assigned_position == position]
                if assigned_students_for_position:
                    for assigned_student, assigned_position in assigned_students_for_position:
                        writer.writerow([course_name, assigned_student, assigned_position.name])
                        report += f"\tAssigned Student: {assigned_student}, Position: {assigned_position.name}\n"
                else:
                    writer.writerow([course_name, 'No student assigned', position.name])
                    report += f"\tNo student assigned, Position: {position.name}\n"

    return report




