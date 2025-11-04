class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def check_price(fruit):
    if fruit.price < 50:
        print(f"{fruit.name} is affordable.")
    else:
        print(f"{fruit.name} is expensive.")

apple = Fruit("Apple", 45)
check_price(apple)
