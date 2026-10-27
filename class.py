class car:
    def __init__(self,model,color,year,for_sale):
        self.model=model 
        self.year=year
        self.color=color
        self.for_sale=for_sale
car1=car("bmw",2024,"red",False)
print(car1.model)

car2=car("audi",2019,"white",True)
print(car2.year)

car3=car("ferrari",2020,"red",True)
print(car3.model)