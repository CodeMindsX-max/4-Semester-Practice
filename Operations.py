import utils
class StudentData:
    def __init__(self, rollno=0, name="", sem=0, cgpa=0.0):
        self.__rollno=rollno
        self.__name=name
        self.__sem=sem
        self.__cpga=cgpa

    @classmethod
    def copy_student(cls,other_student):
        return cls(other_student.__rollno, other_student.__name, other_student.__sem,other_student.__cgpa)

    def addStudent(self):
        self.__rollno=input("Enter your roll no.: ")
        
    