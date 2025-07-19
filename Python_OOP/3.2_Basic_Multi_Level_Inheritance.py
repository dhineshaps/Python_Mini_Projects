class design():
    def ui(self):
        print("This is my system Design")

class curriculam:
    def syllabus(self):
        print("Curriculam loaded")

class mlevel(design,curriculam):  #multi level inheritance
    pass

ft = mlevel()
ft.ui()

print(mlevel.mro())   #method resolution order  # at what priority the methods will be called