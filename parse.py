import pandas as pd


def read_course_ta_requirements(file_path):
    """
    Read the course TA requirements from a CSV file into a dataframe.

    Args:
        file_path (str): The path to the CSV file containing the course TA requirements.

    Returns:
        pd.DataFrame: The course TA requirements dataframe.
    """
    df = pd.read_csv(file_path)
    # Additional preprocessing if needed
    return df


def read_course_director_requests(file_path):
    """
    Read the course director requests from a CSV file into a dataframe.

    Args:
        file_path (str): The path to the CSV file containing the course director requests.

    Returns:
        pd.DataFrame: The course director requests dataframe.
    """
    df = pd.read_csv(file_path)
    # Additional preprocessing if needed
    return df


def read_grad_students_requests(file_path):
    """
    Read the graduate student requests from a CSV file into a dataframe.

    Args:
        file_path (str): The path to the CSV file containing the graduate student requests.

    Returns:
        pd.DataFrame: The graduate student requests dataframe.
    """
    df = pd.read_csv(file_path)
    # Additional preprocessing if needed
    return df


def read_course_director_avoid(file_path):
    """
    Read the course director avoidances from a CSV file into a dataframe.

    Args:
        file_path (str): The path to the CSV file containing the course director preferences.

    Returns:
        pd.DataFrame: The course director preferences dataframe.
    """
    df = pd.read_csv(file_path)
    # Additional preprocessing if needed
    return df


def read_grad_students_avoid(file_path):
    """
    Read the graduate student avoidances from a CSV file into a dataframe.

    Args:
        file_path (str): The path to the CSV file containing the graduate student preferences.

    Returns:
        pd.DataFrame: The graduate student preferences dataframe.
    """
    df = pd.read_csv(file_path)
    # Additional preprocessing if needed
    return df


def read_grad_students_experience(file_path):
    """
    Read the graduate student experience from a CSV file into a dataframe.

    Args:
        file_path (str): The path to the CSV file containing the graduate student experience.

    Returns:
        pd.DataFrame: The graduate student experience dataframe.
    """
    df = pd.read_csv(file_path)
    # Additional preprocessing if needed
    return df


# Step 1: Read course TA requirements
course_ta_requirements_df = read_course_ta_requirements("course_ta_requirements.csv")

# Step 2: Read course director requests
course_director_requests_df = read_course_director_requests("course_director_requests.csv")

# Step 3: Read graduate student requests
grad_students_requests_df = read_grad_students_requests("grad_students_requests.csv")

# Step 4: Read course director avoidances
read_course_director_avoid_df = read_course_director_avoid("course_director_avoid.csv")

# Step 5: Read graduate student avoidances
read_grad_students_avoid_df = read_grad_students_avoid("grad_students_avoid.csv")

# Step 6: Read graduate student experience
grad_students_experience_df = read_grad_students_experience("grad_students_experience.csv")


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
for _, row in course_ta_requirements_df.iterrows():
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
for _, row in course_director_requests_df.iterrows():
    course_name = row['Course']
    director_name = row['Requested TA']

    if course_name not in course_directors:
        course_directors[course_name] = CourseDirector(course_name)

    course_director = course_directors[course_name]
    course_director.requests.append(director_name)

for _, row in read_course_director_avoid_df.iterrows():
    course_name = row['Course']
    ta_to_avoid = row['TAs to Avoid']

    if course_name not in course_directors:
        course_directors[course_name] = CourseDirector(course_name)

    course_director = course_directors[course_name]
    course_director.preferences.append(ta_to_avoid)

# Populate GradStudent class and their requests/preferences/experience
grad_students = {}
for _, row in grad_students_requests_df.iterrows():
    student_name = row['Grad Student']
    requested_courses = row['Desired Courses']

    if student_name not in grad_students:
        grad_students[student_name] = GradStudent(student_name)

    grad_student = grad_students[student_name]
    grad_student.requests.extend(requested_courses.split(','))

for _, row in read_grad_students_avoid_df.iterrows():
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
