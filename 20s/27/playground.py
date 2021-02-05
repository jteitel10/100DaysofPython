def add (*args):
    print(sum(args))

def calculate(n, **kwargs):
    print(kwargs)
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)
calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")

my_car = Car(make='vw')
print(my_car.model, my_car.make)
