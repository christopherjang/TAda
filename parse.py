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
