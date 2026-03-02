# Class Variable are the variable which is declared inside the class without self keyword 
#---> class variable gets life during the class loading("Expor Import mechanism")
#---> class variable are stored in a memory space known as class object 
# Note:-its not reccommanded to access class variable using object reference

class Student:
    college="Govt Eng College" # Creation of class variable
    def __init__(self):
        self.name=None # Instance variable with self keyword
        self.Roll_no=None

s1=Student()
# The object reference which stores inside the object dict,(s1.__dict__)
s1.name="Jack" 
s1.Roll_no=456
#The class variable present inside the class Object memeory ,(s1.__class__.__dict__)
print(Student.college) # Accessing class variable using class name 
print(s1.name," ",s1.Roll_no) # Accessing Instance variable using object reference 

