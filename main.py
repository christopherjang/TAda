# Import necessary functions and classes from the other files
from classes import Course
from parse import read_course_ta_requirements
from parse import read_course_director_requests
from parse import read_grad_students_requests
from parse import read_course_director_avoid
from parse import read_grad_students_avoid
from parse import read_grad_students_experience
from logic import assign_grad_students
from report import generate_assignment_report

# Step 1: Read course TA requirements
course_ta_requirements_df = read_course_ta_requirements("course_ta_requirements.csv")

# Step 2: Read course director requests
course_director_requests_df = read_course_director_requests("course_director_requests.csv")

# Step 3: Read grad student requests
grad_students_requests_df = read_grad_students_requests("grad_student_requests.csv")

# Step 4: Read course director avoids
course_director_avoid_df = read_course_director_avoid("course_director_avoid.csv")

# Step 5: Read grad student avoids
grad_students_avoid_df = read_grad_students_avoid("grad_students_avoid.csv")

# Step 6: Read graduate student experience
grad_students_experience_df = read_grad_students_experience("grad_students_experience.csv")

# Step 7: Populate Course class and its positions
courses = {}
for _, row in course_ta_requirements_df.iterrows():
    course_name = row['Course']
    position_name = row['Position']
    weighting = row['Weighting']

    if course_name not in courses:
        courses[course_name] = Course(course_name)

    course = courses[course_name]
    position = Position(position_name, weighting)
    course.positions.append(position)

# Step 8: Populate CourseDirector class and their requests/preferences
course_directors = {}
for _, row in course_director_requests_df.iterrows():
    course_name = row['Course']
    director_name = row['Requested TA']

    if course_name not in course_directors:
        course_directors[course_name] = CourseDirector(course_name)

    course_director = course_directors[course_name]
    course_director.requests.append(director_name)

for _, row in course_director_avoid_df.iterrows():
    course_name = row['Course']
    ta_to_avoid = row['TAs to Avoid']

    if course_name not in course_directors:
        course_directors[course_name] = CourseDirector(course_name)

    course_director = course_directors[course_name]
    course_director.preferences.append(ta_to_avoid)

# Step 9: Populate GradStudent class and their requests/preferences/experience
grad_students = {}
for _, row in grad_students_requests_df.iterrows():
    student_name = row['Grad Student']
    requested_courses = row['Desired Courses']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.requests.extend(requested_courses.split(','))

for _, row in grad_students_avoid_df.iterrows():
    student_name = row['Grad Student']
    courses_to_avoid = row['Courses to Avoid']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.preferences.extend(courses_to_avoid.split(','))

for _, row in grad_students_experience_df.iterrows():
    student_name = row['Grad Student']
    previous_experience = row['Previous TA Experience']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.experience.extend(previous_experience.split(','))

# Step 10: Assign graduate students to positions
assign_grad_students(courses, course_directors, grad_students)

# Step 11: Generate assignment report
report = generate_assignment_report(courses)

# Print the report
print(report)

# Save the report to a file
with open("assignment_report.txt", "w") as file:
    file.write(report)
