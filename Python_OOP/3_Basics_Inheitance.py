class course:   #parent class
    def __init__(self,name,subject): 
        self.name = name  
        self.subject = subject

    def display(self):
        print("In Parent display")
        return f"name of the mentor is {self.name}"

# to use/call the above class from another class use below 

class fetquest(course):    #Child Class

    def __init__(self, subject ,mentor):
        super().__init__(subject=subject,name=mentor)
        self.mentor = mentor
        self.year=year
        print(f"{self.subject},{self.mentor}")

    def assign_project(self,project):
        print (f"{self.name},{project}")

    def display(self):     # same class we are having in the parent called "Overridding"
        #name of the function should be the same
        super().display()  #if we need to use parent class method then we can use super - so even before override the parent class method can be used
        print(f"name of the mentor is {self.name} of child class")

f1 = fetquest("Dhinesh","Python") # while inherting, we need to pass the parent class parameters
print(f1.name)
print(f1.display())

f2 = fetquest("Dhinesh","Python")
f2.assign_project("LLM")

f2.display()

f3 = fetquest("Python","Dhinesh")