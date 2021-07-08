class Car:

    # Method
    def __init__(self,name, model, price, color) -> None:
        self.carname = name
        self.modeldate = model
        self.price = price
        self.color = color
    
    def run(self):
        print(f"The car name is: {self.carname}")
        print(f"The car model is: {self.modeldate}")
        print(f"The car price is: {self.price}")
        print(f"The car's color is: {self.color}")
    
    
# create object
car_1 = Car("BMW",2017,200000,"blue")

# Run method
car_1.run()
