class course:
    def __init__(self,name,subject):  #declaring variable to class , self points to class 'course', so name and mentor can be passed from user and accessed
        self.name = name  #these variables are attched to the class or this particular instance of class
        self.subject = subject

    def topics(self,topic1,topic2):  #by placing self or any first parameter, we telling that this function is with class or belogs to class and followed by we can have the paramters
        topics_given = f"topics are {topic1} and metor is {self.name}" #class variable can be accesed by self.{variable} name
        return topics_given
    
c1 = course("Dhinesh","Python")  #c1 is the instance which has the value of "Dhinesh" and "Python"
val = c1.topics("oops","web services")


print(c1.name)# we can access the class/instance variable outside the class as thsi

print(val)