def generate_assignment_report(courses):
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


# Call the assignment function
assign_grad_students(courses, course_directors, grad_students)

# Generate the assignment report
report = generate_assignment_report(courses)

# Print the report
print(report)

# Save the report to a file
with open("assignment_report.txt", "w") as file:
    file.write(report)
