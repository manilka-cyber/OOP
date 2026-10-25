class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self,address):
    print(self.firstname, self.lastname, address)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname("colombo")

