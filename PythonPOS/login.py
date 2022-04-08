
try:
    StudentName = str(input("Enter your Name: "))
    StudentID = int(input("Enter Student ID: "))
    Year = int(input("Enter Year: "))
    Course = str(input("Enter Course: "))
    Section = str(input("Enter Section: "))
except Exception as error:
    print(error)

credentials = {
    "StudentName" : StudentName,
    "StudentID": StudentID,
    "Year" : Year,
    "Course" : Course,
    "Section" : Section,
    "Budget" : 150
}





