class Employee:

    def __init__(self):
        self.emp_name=None
        self.emp_sal=None

    def display_info(self):
        print(self.emp_name," ",self.emp_sal)

emp1=Employee()
emp1.emp_name="Jack"
emp1.emp_sal=25000
emp1.display_info()

emp2=Employee()
emp2.emp_name="Jacob"
emp2.emp_sal=35000
emp2.display_info()