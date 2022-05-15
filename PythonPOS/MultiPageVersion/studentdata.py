class Student():
    def __init__(self,name:str,id:str,year:str,course:str,section:str):
        self.name = name
        self.id = id
        self.year = year
        self.course = course
        self.section = section

while True:
    try:
        name251:str = str(input("Input Name Here: "))
        id251:str = str(input("Input Id Here: "))
        year251:str = str(input("Input Year Here: "))
        course251:str = str(input("Input Course Here: "))
        section251:str = str(input("Input Section Here: ")) 
        break
    except Exception as error:
        print(error)

USER = Student(name251,id251,year251,course251,section251)

iterable = {
    "Name": USER.name,
    "ID": USER.id,
    "Year": USER.year,
    "Course": USER.course,
    "Section": USER.section
}