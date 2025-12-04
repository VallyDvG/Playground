class student:
    def __init__(self,nume_student:str) -> None:
        self.nume_student=nume_student

        
class curs:
    def __init__(self,titlu:str) -> None:
        self.titlu=titlu
        self.lista_studenti=[]

    def adauga_student(self,student:object) ->None:
        self.student=student
        self.lista_studenti.append(student)

    def afiseaza_studenti(self):
        print(f"Studenți înscriși la cursul {self.titlu}:")
        for s in self.lista_studenti:
            print("-", s.nume_student)

# ----- Testare -----
s1 = student("Ana")
s2 = student("Mihai")
s3 = student("Iulia")

c = curs("Programare Python")

c.adauga_student(s1)
c.adauga_student(s2)
c.adauga_student(s3)

c.afiseaza_studenti()