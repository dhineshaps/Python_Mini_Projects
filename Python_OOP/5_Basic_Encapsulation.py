class mentor():
    def __init__(self,name, course):
        self._name = name   #if _ is placed before variable it is kinf of protectoion and needs to be called with _
        self.__course = course                   #access modifier concept - public, private, protected
                 #__ is private , we can't able to call it directly

    def get_name(self):
        return self.__course
            
m1 = mentor("Dhinesh","LLM")
print(m1._name)
print(m1._name)

#To Access the __ variable we have to follow the below

print(m1._mentor__course)  #mangling the variable or getter and setter can be used

print(m1.get_name())