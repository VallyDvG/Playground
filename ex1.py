from datetime import date 

class Not_valid(ValueError):
    '''Custom exception for invalid year'''
    pass

class Car:
    '''Class representing a car with brand and year attributes'''
    year_today=date.today().year
    def __init__(self, brand:str, year:int):
        '''Initialize Car with brand and year, calculate age, and validate year'''
        self.brand=brand
        self.year=year
        self.age=self.year_today-self.year
        if self.year>2025:
            raise Not_valid("This is not a valid year")
        
    def show_attributes(self):
        '''Return a string with the car's brand and year attributes and their values'''
        return f"The car brand is: {self.brand} and the year:{self.year}" 
    

    def show_age(self):
        '''Return a string indicating the age of the car in years'''
        if self.age < 2:
            return f"{self.age} year"
        else:
            return f"{self.age} years"

logan=Car("Dacia Logan",2015)
tesla=Car("Tesla", 2024)

print(f"Brand: {logan.brand}",f",Year: {logan.year},")
print(logan.show_attributes())
print(logan.show_age())

print(f"Brand: {tesla.brand}",f", Year: {tesla.year},")
print(tesla.show_attributes())
print(tesla.show_age())