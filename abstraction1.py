#abstraction means hinding unnecesary information

from abc import ABC,abstractmethod

#abstract method in abstract class has defination but not implementation

class car(ABC):

    @abstractmethod
    #we can also create constructor in abstract class

    def performance(self):
       pass

#we cant create object for abstract class

#we can not use abstract class methods in child calss or subclasses with out implementation
class suzuki(car):

    def performance(self):
        print("milage is 40kmpl")

t1=suzuki()
t1.performance()

class ignis(car):

    def performance(self):
        print("milage is 50 kmpl")

class beleno(car):

    def performance(self):
        print("milage is 60 kmpl")

h1=ignis()
tt2=beleno()

t1.performance()
h1.performance()
tt2.performance()



class A(ABC):

    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class B(A):

    def m1(self):
        print("hai")

#here we cant create object of class N because m2 method is not implemanted if we create it shows error
# so CLASS B also acting as base class or parent class
# b=B()
#b.m1()  #here it is showung error

class C(B):

    #here we can implement m2 @abstract method
    def m2(self):
        print("hello")

class D(A):

    def m1(self):
        print("hai narayana")

    def m2(self):
        print("hai rajesh")


#here both CLASS A AND B are acting as base clases
d=D()
d.m1()
d.m2()
c=C()
c.m2()
c.m1()

#b.B() #here we can create objet B also act  as base class


#__init__ in abstrection class

class caluclation:

    def __init__(self,value):
        self.value=value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class result(caluclation):

    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value-50)

result_add=result(100)
result_sub=result(100)
result_add.add()
result_sub.sub()

from abc import ABC,abstractmethod

class applications(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def features(self):
        pass

class youtube(applications):

    def run(self):
        print("the application is running sucessfully")

    def features(self):
        print("all features of youtube is working")

youtube_music=youtube()
youtube_music.run()











