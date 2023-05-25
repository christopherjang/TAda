# Import necessary functions and classes from the other files
from parse import read_course_ta_requirements
from parse import read_course_director_requests
from parse import read_grad_student_requests
from parse import
from logic import assign_grad_students
from report import generate_assignment_report

# Step 1: Read course TA requirements
courses = read_course_ta_requirements("course_ta_requirements.csv")

# Step 2: Read course director requests
course_directors = read_course_director_requests("course_director_requests.csv")

# Step 3: Read grad student requests
grad_students = read_grad_student_requests("grad_student_requests.csv")

# Step 4: Assign graduate students to positions
assign_grad_students(courses, course_directors, grad_students)

# Step 5: Generate assignment report
report = generate_assignment_report(courses)

# Print the report
print(report)

# Save the report to a file
with open("assignment_report.txt", "w") as file:
    file.write(report)
