class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"

class Libreria:
    def __init__(self):
        self.catalogo = []
    
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Libro aggiunto: {libro.descrizione()}")
        
    def rimuovi_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print(f"Libro con ISBN {isbn} rimosso.")
                return
        print("Libro non trovato.")
        
    def cerca_per_titolo(self, titolo):
        risultati = [libro for libro in self.catalogo if libro.titolo.lower() == titolo.lower()]
        return risultati
    
    def mostra_catalogo(self):
        if not self.catalogo:
            print("La libreria è vuota.")
        else:
            print("Catalogo della libreria:")
            for libro in self.catalogo:
                print(libro.descrizione())
