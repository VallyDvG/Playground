class TemperatureSensor:

    min_safe=0
    max_safe=40
    def __init__(self, location:str, temperature:float):
        self.location=location
        self.temperature=temperature
        self.alert()

    def is_safe(self) ->bool:
        if self.temperature >self.min_safe and self.temperature < self.max_safe:
            self.alert()
            return True

        else:
            return False
        
    def __str__(self):
        return(f"Temperature is {self.temperature}")


    def update_temperature(self, value:float):
        self.temperature=value
        self.alert()
        return self.temperature
    
    def alert(self) :
            if self.temperature <self.min_safe or self.temperature > self.max_safe:
                print("Temperature is dangerous, please update temperature using update_temperature() method")
            else:
                print("Temperature is not dangerous")


bucatarie=TemperatureSensor("bucatarie",42.5)

bucatarie.update_temperature(39)
bucatarie.update_temperature(41)

# print(bucatarie.is_safe())

# bucatarie.update_temperature(50)

# print(bucatarie)

# print(bucatarie.is_safe())