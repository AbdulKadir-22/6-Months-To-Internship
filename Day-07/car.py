class Car:
    def __init__(self,name,model,color,for_sale):
        self.name = name
        self.model = model
        self.color = color
        self.for_sale = for_sale

    def describe(self):
        print(f"Your car is a {self.model} {self.name} of {self.color} color")