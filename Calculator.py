class Calculator:
    def __init__(self):
        self.a=int(input("Enter the value of a: "))
        self.b=int(input("Enter the value of b: "))

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):  
        if self.b==0:
            return "Division by zero is not allowed"
        return self.a/self.b
calc=Calculator()
print("Addition: ",calc.add())
print("Subtraction: ",calc.sub())
print("Multiplication: ",calc.mul())
print("Division: ",calc.div())