class Punto:
    def __init__(self, x, y):
        """
        Inizializza un punto con coordinate x e y.
        """
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        """
        Modifica le coordinate del punto.
        """
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        """
        Restituisce la distanza del punto dall'origine (0,0).
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        """
        Rappresentazione stringa del punto.
        """
        return f"Punto({self.x}, {self.y})"

# Esempio di utilizzo
p = Punto(3, 4)
print(p)  
print("Distanza dall'origine:", p.distanza_da_origine())  
p.muovi(1, -2)
print(p)  
print("Distanza dall'origine:", p.distanza_da_origine())

