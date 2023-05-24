# Print Course information
for course_name, course in courses.items():
    print(f"Course: {course_name}")
    for position in course.positions:
        print(f"- Position: {position.name}, Weighting: {position.weighting}")
    print()

# Print Course Director information
for course_name, course_director in course_directors.items():
    print(f"Course: {course_name}")
    print(f"- Requested TAs: {', '.join(course_director.requests)}")
    print(f"- TAs to Avoid: {', '.join(course_director.preferences)}")
    print()

# Print Grad Student information
for student_name, grad_student in grad_students.items():
    print(f"Grad Student: {student_name}")
    print(f"- Requested Courses: {', '.join(grad_student.requests)}")
    print(f"- Courses to Avoid: {', '.join(grad_student.preferences)}")
    print(f"- Previous TA Experience: {', '.join(grad_student.experience)}")
    print()