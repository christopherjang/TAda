def assign_grad_students(courses, course_directors, grad_students):
    assigned_students = set()  # Set to keep track of assigned students

    for course_name, course in courses.items():
        print(f"Assigning grad students for {course_name}:")
        positions = course.positions

        # Get the course director requests for the current course
        if course_name in course_directors:
            course_director = course_directors[course_name]
            director_requests = course_director.requests
        else:
            director_requests = []

        for position in positions:
            print(f"\nPosition: {position.name}")

            # Get the grad students who meet the criteria and have not been assigned to another course
            available_students = [student for student in grad_students.values()
                                  if (course_name in student.requests or student.name in director_requests) and
                                  all(course_name not in student.preferences for course_name in position.preferences) and
                                  course_name in student.experience and
                                  student.name not in assigned_students]

            # Sort the available students based on previous experience and weighting
            sorted_students = sorted(available_students, key=lambda s: (position.weighting, -len(s.experience)), reverse=True)

            if sorted_students:
                assigned_student = sorted_students[0]
                assigned_student.experience.append(course_name)  # Update the student's experience
                assigned_students.add(assigned_student.name)  # Add student to assigned set
                print(f"Assigned: {assigned_student.name}")
            else:
                print("No suitable grad student available")

    print("\nAssignment process completed.")

# Call the assignment function
assign_grad_students(courses, course_directors, grad_students)
