# ----> Instance method:  Declared inside the class and it uses "self " as implicit parameter 
# Intance method are stored in class object memory and we can access it using object reference or reference variable
# We cannot access the instance methiod using class name because instance method accept "SELF" as implicit parameter


class Wedding:
    
    #Behaviour of the class
    def ring(self,BrideName,GroomName):    # Instance method of the class
        self.BrideName=BrideName # Instance variable with self keyword
        self.GroomName=GroomName # Instance variable with self keyword

        # Accessing the instance variable using self keyword and print the statement
        print(f"{self.GroomName} put the ring on {self.BrideName}'s finger") 

    def eat(self): # Instance method of the class
        print("Eat the wedding cake")

    
# We cannot access the instance methiod using class name because instance method accept "SELF" as implicit parameter 

w1=Wedding() # Object creation and calling the method of the class using the object
w1.ring("Mary" ,"Gorge")  # Calling the method of the class using the object
w1.eat()  # Calling the method of the class using the object

print(w1.__class__.__dict__)