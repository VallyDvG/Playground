class angajat:
    def __init__(self,nume,salariu):
        self.nume=nume
        self.salariu=salariu

    def descriere(self):
        return f"{self.nume} are salariul {self.salariu}"
    
class itst(angajat):
    def __init__(self, nume, salariu, departament):
        super().__init__(nume,salariu)
        self.departament=departament

    def descriere(self):
        baza=super().descriere()
        return f"{baza} si este din departamentul: {self.departament}"
    
class manager(angajat):
    def __init__(self, nume, salariu, departament):
        super().__init__(nume,salariu)
        self.departament=departament

    def descriere(self):
        baza=super().descriere()
        return f"{baza} si este din departamentul: {self.departament}"

ion=itst("Ion",1000,"IT")
maria=manager("Maria",2000,"management")

print(ion.descriere())
print(maria.descriere())