class Person: # class creation with name Person
    # Method / Function
    def __init__(self): # self is a key word which stores the address of current executing object
        # Instance variable =" A variable which is declared inside the class using self keyword"
        self.name="Jack"
        self.ID=1203 
        self.contact_no=8256970223  
# Object Creation
p1=Person()
print(p1.name,"  ",p1.contact_no,"  ",p1.ID) # Object reference is used to access the instance variable
