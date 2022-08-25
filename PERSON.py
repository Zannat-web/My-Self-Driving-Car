class Person:
     def __init__(self,name,age=0):
         self.name = name
         self.__age = age
     def display(self):
         print(self.name)
         print(self.__age)

     def getAge(self):
          print(self.__age)

     def setAge(self):
         self.__age = age
Person = Person('Dev', 30)
Person.setAge(35)
Person.getAge()
