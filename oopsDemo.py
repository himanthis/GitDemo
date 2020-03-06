# classes are user defined blue print or prototype
# sum,multiplication,addition
# methods,variables,instance variable,constructor
# objects for your classes

#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self,a,b):
        self.first=a
        self.second=b
        print("I am called automatically when object is created")

    def getData(self):
        print("i am now executing as method class")

    def Summation(self):
        return self.first + self.second+ self.num # Calculator.num


obj = Calculator(2,3)  # syntax to create objects in python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4,5)  # syntax to create objects in python
obj1.getData()
print(obj1.Summation())