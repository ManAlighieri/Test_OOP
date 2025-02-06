#Arreglos
class Galletas:
    def __init__(self,galletas,chocolate,vanilla):
        self.galletas = galletas
        self.chocolate = chocolate
        self.vanilla = vanilla

    def display(self):
        print(f"TOTAL GALLETAS: {self.galletas}")
        print(f"TOTAL GALLETAS: {self.chocolate}")
        print(f"TOTAL GALLETAS: {self.vanilla}")

mis_galletas = Galletas(50,20,30)
mis_galletas.display()

        
     
