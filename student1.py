class Student:
    def __init__(self):
        # Instance variable can create inside the class and also outside the class 
        self.Roll_no=None # intsance variable creation type 1
        self.Name=None # intsance variable creation type 1

# object 1 is created...
s1=Student()
s1.Name="Jack"
s1.Roll_no=101
# Creating outside the call and inside the object
s1.contact=8256970223  # Creating an Instance variable type-2
s1.marks=90
print(s1.Name," ",s1.Roll_no," ",s1.contact," ",s1.marks)

# object 2 is created...
s2=Student()
s2.Name="James"
s2.Roll_no=102
# Creating outside the call and inside the object
s2.contact=8256970652  # Creating an Instance variable type-2
s2.marks=85
print(s2.Name," ",s2.Roll_no," ",s2.contact," ",s2.marks)

