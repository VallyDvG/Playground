from datetime import date 

class Not_valid(ValueError):
    pass

class Car:
    year_today=date.today().year
    def __init__(self, brand:str, year:int):
        self.brand=brand
        self.year=year
        self.age=self.year_today-self.year
        if self.year>2025:
            raise Not_valid("This is not a valid year")
        
    def show_attributes(self):
        return f"The car brand is: {self.brand} and the year:{self.year}" 
    

    def show_age(self):

        if self.age < 2:
            return f"{self.age} year"
        else:
            return f"{self.age} years"

logan=Car("Dacia Logan","2035")
tesla=Car("Tesla", 2024)

print(f"Brand: {logan.brand}",f",Year: {logan.year},")
print(logan.show_attributes())
print(logan.show_age())

print(f"Brand: {tesla.brand}",f", Year: {tesla.year},")
print(tesla.show_attributes())
print(tesla.show_age())