class mentor():
    total_course = 0   #class variable
    def __init__(self,name):
        self.name = name
        mentor.total_course += 1   #to utilize the class variable

    def introduction(self):   #instance method
        return f"I am a mentor {self.name} on fetquest"

    @classmethod
    def get_total_course_taken(cls): #here cls given because it belongs to class, self belongs to the instance we creating
        return cls.total_course
    
    @staticmethod
    def is_valid_email(email):  #here no self is given, it act as static method
        return "@" in email and "." in email


m = mentor("Dhinesh") #creating the instance using the m object

print(m.introduction())

fet1 = mentor("Dhinesh")
print(fet1.total_course)
print(fet1.get_total_course_taken())
fet2 = mentor("fets")
print(fet2.total_course)
print(fet2.get_total_course_taken())

print(mentor.total_course)  # to directly access the class variable

print(mentor.is_valid_email("dhi@gm.com"))  # can be accssed using the class name.func_name()