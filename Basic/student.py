class Student:
    def __init__(self):
        # it stores the address of the current executing object
        # self keyword keeps updating as we create the new objects
        print("I am self..",self) # in this case the adress is :- s1= 0x00000272C566CFE0 and s2=0x00000272C566CFB0


s1=Student() 
print("i am object ref..",s1) # s1= 0x00000272C566CFE0

s2=Student() #s2=0x00000272C566CFB0
print(" I object ref...",s2)