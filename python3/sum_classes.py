#Classes in python3 are a lot easier to work with

class Numbers:

    #Constructor
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    #Add method to find the sum between the two given numbers
    def add(self):
        sums = self.num1 + self.num2
        print(sums)

    #Subtract method
    def subtract(self):
        sub = self.num1 - self.num2
        print(sub)

    #Multiplication method
    def multiplication(self):
        mul = self.num1 * self.num2
        print(mul)

    #Division method
    def division(self):
        div = self.num1 / self.num2
        print(div)

#Making a new object of Numbers class
new_object = Numbers(7,4)

#Using the new object to call the methods in the class
new_object.add()
new_object.subtract()
new_object.multiplication()
new_object.division()