class sold_insuficient(ValueError):
    pass

class valori_negative(ValueError):
    pass

class deschide_depozit:
    def __init__(self,titular:str,sold:int) -> None:
        self.titular=titular
        self._sold=sold

    def depune(self,suma:int):
        if suma < 0:
            raise valori_negative("Nu se poate")
        else:
            self._sold+=suma
    
    def retrage(self,suma):
        if suma > self._sold:
            raise sold_insuficient("sold insuficient")
        else:
            self._sold-=suma
    
    def afiseaza_sold(self):
        print(f"Soldul curent pentru titularul:{self.titular} este {self._sold}")


cont1=deschide_depozit("Ion",1000)
cont2=deschide_depozit("Maria",2000)

cont1.depune(500)
cont2.retrage(1000)

cont1.afiseaza_sold()
cont2.afiseaza_sold()