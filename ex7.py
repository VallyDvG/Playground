class animal:
    def __init__(self,nume):
        self.nume=nume

class caine(animal):
    def __init__(self):
        pass
    def vorbeste(self):
        print("HAM")

class vaca(animal):
    def __init__(self):
        pass
    def vorbeste(self):
        print("MUU")

c=caine()
c.vorbeste()

v=vaca()
v.vorbeste()