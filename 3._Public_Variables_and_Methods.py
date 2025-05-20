class Car:
    def __init__(self, brand):
        self.brand = brand 

    def start(self):
        print(f"Car Brand : {self.brand}")    

my_car = Car("Toyota")
print(f"The Public Variable is : {my_car.brand}")
my_car.start()