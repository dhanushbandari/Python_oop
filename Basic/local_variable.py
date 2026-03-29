class Cloths:

    dealer ='YOUSTA' # Class Variable It can acess only using Class name 

    def __init__(self ,name,brand,price):
        self.name=name # Instance variable with self keyword
        self.brand=brand # Instance variable with self keyword
        self.price=price  # Instance variable with self keyword

        # Cannot access the Local variable outside the method
        tax=self.price*0.18
        totalPrice=tax+self.price # Local Variable which is created inside the method and its life is only inside the method and we cannot access it outside the method
        print("The Total Price of the cloths is: ",totalPrice)  


# Object creation and passing the value to the constructor and the constructor will call the method which is present inside the class and the method will calculate the total price of the cloths and print it
c1=Cloths("NIKE","Sports",int(input("Enter the price of the cloths: "))) 
print(Cloths.dealer," ",c1.name," ",c1.brand," ",c1.price,)

c2=Cloths("ADIDAS","Sports",int(input("Enter the price of the cloths: ")))
print(Cloths.dealer," ",c2.name," ",c2.brand," ",c2.price,)