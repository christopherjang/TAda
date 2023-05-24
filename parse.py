import pandas as pd

# Read the dataset from the CSV files
ta_requirements_path = 'course_ta_requirements.csv'
df_ta_requirements = pd.read_csv(ta_requirements_path)

director_requests_path = 'course_director_requests.csv'
df_director_requests = pd.read_csv(director_requests_path)

director_preferences_path = 'course_director_preferences.csv'
df_director_preferences = pd.read_csv(director_preferences_path)

student_requests_path = 'grad_students_requests.csv'
df_student_requests = pd.read_csv(student_requests_path)

student_preferences_path = 'grad_students_preferences.csv'
df_student_preferences = pd.read_csv(student_preferences_path)

student_experience_path = 'grad_students_experience.csv'
df_student_experience = pd.read_csv(student_experience_path)

class Course:
    def __init__(self, name):
        self.name = name
        self.positions = []

class Position:
    def __init__(self, name, weighting):
        self.name = name
        self.weighting = weighting

class CourseDirector:
    def __init__(self, name):
        self.name = name
        self.requests = []
        self.preferences = []

class GradStudent:
    def __init__(self, name):
        self.name = name
        self.requests = []
        self.preferences = []
        self.experience = []

# Populate Course class and its positions
courses = {}
for _, row in df_ta_requirements.iterrows():
    course_name = row['Course']
    position_name = row['Position']
    weighting = row['Weighting']

    if course_name not in courses:
        courses[course_name] = Course(course_name)

    course = courses[course_name]
    position = Position(position_name, weighting)
    course.positions.append(position)

# Populate CourseDirector class and their requests/preferences
course_directors = {}
for _, row in df_director_requests.iterrows():
    course_name = row['Course']
    director_name = row['Requested TA']

    if course_name not in course_directors:
        course_directors[course_name] = CourseDirector(course_name)

    course_director = course_directors[course_name]
    course_director.requests.append(director_name)

for _, row in df_director_preferences.iterrows():
    course_name = row['Course']
    ta_to_avoid = row['TAs to Avoid']

    if course_name not in course_directors:
        course_directors[course_name] = CourseDirector(course_name)

    course_director = course_directors[course_name]
    course_director.preferences.append(ta_to_avoid)

# Populate GradStudent class and their requests/preferences/experience
grad_students = {}
for _, row in df_student_requests.iterrows():
    student_name = row['Grad Student']
    requested_courses = row['Desired Courses']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.requests.extend(requested_courses.split(','))

for _, row in df_student_preferences.iterrows():
    student_name = row['Grad Student']
    courses_to_avoid = row['Courses to Avoid']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.preferences.extend(courses_to_avoid.split(','))

for _, row in df_student_experience.iterrows():
    student_name = row['Grad Student']
    previous_experience = row['Previous TA Experience']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.experience.extend(previous_experience.split(','))
