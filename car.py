class Car:

    delearship = "Lamborghini" # Class Attribute
    delearship2= "Ferrari" # Class Attribute

    def __init__(self):
        self.model= "Aventador"
        self.year = 2020
        self.color = "Yellow"
        self.price = None


c1=Car()
c1.price = float(input("Enter the price of the car: "))
print(Car.delearship," ",c1.model," ",c1.year," ",c1.color," ",c1.price)


tax= c1.price * 0.18 # Calculating the tax of the car using the price attribute of the class
totalPrice =tax + c1.price # Calling The price using object reference variable c1
print("The Total Price of the car is: ",totalPrice)

c2=Car()
c2.price = float(input("Enter the price of the car: "))
print(Car.delearship2," ",c2.model," ",c2.year," ",c2.color," ",c2.price)

tax= c2.price * 0.20 # Calculating the tax of the car using the price attribute of the class
totalPrice =tax + c2.price # Calling The price using object reference variable c2
print("The Total Price of the car is: ",totalPrice)
