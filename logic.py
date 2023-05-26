from classes import *

def assign_grad_students(courses, course_directors, grad_students):
    assigned_students = []  # List to keep track of assigned students

    for course_name, course in courses.items():
        print(f"Assigning grad students for {course_name}:")
        positions = course.positions

        # Get the course director requests for the current course
        if course_name in course_directors:
            course_director = course_directors[course_name]
            director_requests = course_director.requests
        else:
            director_requests = []

        # Get the grad student requests for the current course
        if course_name in grad_students:
            student_requests = grad_students[course_name].requests
        else:
            student_requests = []

        # Get the course director avoids for the current course
        if course_name in course_directors:
            course_director = course_directors[course_name]
            director_avoids = course_director.avoid
        else:
            director_avoids = []

        # Get the graduate student avoids for the current course
        if course_name in grad_students:
            student_avoids = grad_students[course_name].avoid
        else:
            student_avoids = []

        for position in positions:
            print(f"\nPosition: {position.name}")

            # Get the grad students who have not been assigned to another course
            available_students = [student for student in grad_students.values()
                                  if student.name not in [name for name, _ in assigned_students]]

            # Sort the available students based on previous experience, director requests, weighting, and course requests
            sorted_students = sorted(available_students, key=lambda s: (
                1 if course_name in s.experience else 0,
                # Assign a higher value if the student has prior experience teaching the course
                2 if s.name in director_requests else 0,
                # Assign a higher value if the student is indicated in director requests
                position.weighting,
                # Assign a higher value for higher weight courses
                -3 if s.name in director_avoids else 0,
                # Assign a lower value for students that directors wish to avoid
                -1 if course_name in student_avoids else 0,
                # Assign a lower value if a student does not wish to teach the course
            ), reverse=True)

            if sorted_students:
                assigned_student = sorted_students[0]
                assigned_students.append((assigned_student.name, position))  # Store the assigned student with the position object
                print(f"Assigned: {assigned_student.name}")
            else:
                print("No suitable grad student available")

    print("\nAssignment process completed.")
    return assigned_students
