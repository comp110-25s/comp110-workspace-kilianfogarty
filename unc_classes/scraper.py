import requests
from bs4 import BeautifulSoup
import csv

# URL of the page
url = "https://catalog.unc.edu/undergraduate/ideas-in-action/communication-beyond/"

# Fetch and parse the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all <a> tags with class="bubblelink code"
course_links = soup.find_all("a", class_="bubblelink code")

# Extract course codes like "ANTH 432"
courses = set()
for link in course_links:
    text = link.get_text().replace(
        "\xa0", " "
    )  # Replace non-breaking space with regular space
    if text:
        courses.add(text.strip())

# Print sorted list
for course in sorted(courses):
    print(course)

# Export to CSV
with open("comm.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Course"])  # header
    for course in sorted(courses):
        writer.writerow([course])

print("✅ Courses saved to unc_courses.csv")
