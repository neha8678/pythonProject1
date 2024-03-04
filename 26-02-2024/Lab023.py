class Person:
     #Class Variables/ Instance Variables
    name= None
    age= None

    def Walk(self):
         a = 10 #Local Variable
         print("Hello your name is " , self.name)
         print("Hello your age is" , self.age)
         print(a)

Neha=Person()
Neha.Walk()