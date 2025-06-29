class course:
    ''' constructor is the special method which is goung to ask some data here it is name and mentor'''
    ##creating constructor using self abd below is the special method #########################################################
    def __init__(self,name,subject):  #declaring variable to class , self points to class 'course', so name and mentor can be passed from user and accessed
        self.name = name  #these variables are attched to the class or this particular instance of class
        self.subject = subject

    def __str__(self):
        return f"hello pythonista, name of the mentor is {self.name}"

    ############################################################################################

    def __eq__(self,value):  #comapres one instance variable with another instance variable c1.name == c2.name
        return self.name == value.name

    ##############################################################################################

    def __len__(self):
        return self.name

    #######################################################################

    #to delete the object
    # def __del__(self):
    #     print("Object will be deleted")

    #######################################################################

    #call will act as function

    def __call__(self):
        return f"{self.name}"

    ###################################################

c1 = course("Dhinesh","Python")
print(c1.name)
print(c1) #by printing this it will give the hexa decimal i.e  <__main__.course object at 0x7a997a3e3950> but if you want to print something out of it 
          # special method __str__ can be used, irresective of how many variables are       

########## __eq__ spl method  ######
c2 = course("Dhinesh", "LLM")

print(c1 == c2)

########### __len__ spl method ###########

c3 = course("Dhinesh",["python","llm","AI"])

print(len(c3.name)) #dhinesh -> 7
print(len(c3.subject)) # even the subject is not decalred it can be accssed as it works on the whole object c3

################

#print(del(c3))


#############
# call - use spl method as function - calling the obejct as function

print(c3())