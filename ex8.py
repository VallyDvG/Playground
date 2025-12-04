class masina:
    def __init__(self,marca):
        self.marca=marca
    
    def descriere(self):
        return f"Este o masina marca {self.marca}"
    
class model(masina):
    def __init__(self,marca,model):
        self.model=model
        super().__init__(marca)
    
    def descriere(self):
        baza=super().descriere()
        return f"{baza}, iar modelul este: {self.model}"
    
bmw=masina("bmw")
print(bmw.descriere())

audi=model("Audi","a3")
print(audi.descriere())

class masina_electrica(model):
    def __init__(self,marca,model,baterie):
        super().__init__(marca,model)
        self.baterie=baterie
    
    def descriere(self):
        baza=super().descriere()
        return f"{baza} si are bateria, {self.baterie}"


me=masina_electrica("tesla","a",55)

print(me.descriere())