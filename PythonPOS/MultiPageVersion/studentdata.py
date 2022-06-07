class Student():
    def __init__(self,name:str,id:int,year:str,course:str,section:str):
        self.name = name
        self.id = str(id)
        self.year = year
        self.course = course
        self.section = section

while True:
    try:
        name251:str = str(input("Input Name Here: "))
        id251:int = int(input("Input Id Here: "))
        year251:str = str(input("Input Year Here: "))
        course251:str = str(input("Input Course Here: "))
        section251:str = str(input("Input Section Here: ")) 
        print("Name: " + name251 + "\n" \
            + "ID: " + str(id251) + "\n" \
            + "Year: " + year251 + "\n" \
            + "Course: " + course251 + "\n" \
            + "Section: " + section251)
        confirmation:str = str(input('Confirm Input? y/n: '))
        if confirmation.lower() == 'y':
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