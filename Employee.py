class Employee:

    def __init__(self):
        self.emp_name=None # Instance variable with self keyword 
        self.emp_sal=None  # Instance variable with self keyword

    def display_info(self):
        print(self.emp_name," ",self.emp_sal) # Accessing Instance variable using self keyword inside the class method

emp1=Employee() # object 1 is created and the address of the object is stored in emp1 reference variable
emp1.emp_name="Jack"
emp1.emp_sal=25000
emp1.display_info() # Accessing Instance variable using object reference and the object reference is stored in emp1 and emp2

emp2=Employee() # object 2 is created and the address of the object is stored in emp2 reference variable
emp2.emp_name="Jacob"
emp2.emp_sal=35000
emp2.display_info() # Accessing Instance variable using object reference and the object reference is stored in emp1 and emp2