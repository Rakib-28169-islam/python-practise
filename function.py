def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 
#------------------------------------------------------
def hello(name='rakib')
    return f"My Name is {name}"

bio = hello()
print(bio)
#------------------------------------------------------
def myFun(n):
    return lambda a: a*n  
res = myFun(2)
print(res(11))
#------------------------------------------------------
#class object
class Car:
     def __init__(self,name,age):
         self.name = name
         self.age = age
 
     def __str__(self):
         return f"Name:{self.name} Age:{self.age}"
         
         
bio = Car('esha',23)
print(bio)
#----------------------------------------------------------
#inheritance

class animal:
     def __init__(self,name):
         self.name = name
         
     
class cat(animal):
      def __init__(self,name):
          super().__init__(name)
          self.sound = 'meawwwwo!!'
          
      def __str__(self):
          return f"animal:{self.name} and Sound:{self.sound}"
         
class dog(animal):
      def __init__(self,name):
          super().__init__(name)
          self.sound = 'ghow ghow!!'
          
      def __str__(self):
          return f"animal:{self.name} and Sound:{self.sound}" 
          
          
o1 = cat('parshian')
o2 = dog('german-shepad')

print(o1)
print(o2)
#---------------------------------------------------------------
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


         
