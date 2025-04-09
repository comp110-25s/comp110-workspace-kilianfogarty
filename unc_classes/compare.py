import pandas as pd

# Load the master spreadsheet
master = pd.read_csv("comm.csv")
# Load the other four spreadsheets
create = pd.read_csv("create.csv")
past = pd.read_csv("past.csv")
globa = pd.read_csv("global.csv")
power = pd.read_csv("power.csv")

# Define the column name that contains course info
course_column = "Course"  # Change this to match the actual column name

# Convert to sets for comparison (and clean whitespace)
master_courses = set(master[course_column].str.strip())


# Function to count overlap
def count_shared(sheet, name) -> None:
    courses = set(sheet[course_column].str.strip())
    shared = master_courses.intersection(courses)
    print(f"{shared} shared with {name}")
    return None


# Compare and print
count_shared(create, "create")
count_shared(past, "past")
count_shared(globa, "global")
count_shared(power, "power")
