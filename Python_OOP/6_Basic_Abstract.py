from abc import ABC, abstractmethod

#abscraction is more of creating a skeleton and utilizing it

class mentor(ABC):  #BASE Class
     
    @abstractmethod 
    def teach(self):
        pass

    @abstractmethod
    def course(self):
        pass


class fetmentors(mentor):  # this class can have all the above function

    def teach(self):
        return "this will be teaching"

    def course(self):
        return "this is course"

fet = fetmentors()
print(fet.course())

#we can't never use - creating obj or instance of abstect class