class MyClass:
  x = 5
  y = 10
  z = 100
  
print(MyClass)

p1 = MyClass()
print(p1.x)
print(p1.y)

del p1

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.y)
print(p3.z)


class person:
    
    pass