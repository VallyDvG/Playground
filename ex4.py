class Termometru:
    def __init__(self,value) :
        self._minimum_value=-273.15
        self.value=value
    
    def in_farenheit(self):
        self.conversie=(self.value*1.8)+32
        if self.value<self._minimum_value:
            return ("Impossible")
        else:
            return self.conversie

a=Termometru(222)

print(a.in_farenheit())
