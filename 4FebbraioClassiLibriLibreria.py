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
                
# Creazione di una libreria
libreria = Libreria()

# Creazione e aggiunta di libri
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "9788804668239")
libro2 = Libro("1984", "George Orwell", "9780451524935")
libro3 = Libro("1984", "George Orwell", "9780141036144")

libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)

# Mostrare il catalogo
libreria.mostra_catalogo()

# Ricerca per titolo
risultati = libreria.cerca_per_titolo("1984")
print("\nRisultati ricerca per titolo '1984':")
for libro in risultati:
    print(libro.descrizione())

# Rimozione di un libro
libreria.rimuovi_libro("9780451524935")

# Mostrare il catalogo aggiornato
libreria.mostra_catalogo()
