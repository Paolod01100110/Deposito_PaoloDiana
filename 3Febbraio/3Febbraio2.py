class Libro:
    def __init__(self, titolo, autore, pagine):
        """
        Inizializza un libro con titolo, autore e numero di pagine.
        """
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        """
        Restituisce una stringa con le informazioni del libro.
        """
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha {self.pagine} pagine."

    def __repr__(self):
        """
        Rappresentazione stringa del libro.
        """
        return f"Libro('{self.titolo}', '{self.autore}', {self.pagine})"

# Esempio di utilizzo
libro = Libro("1984", "George Orwell", 328)
print(libro)  
print(libro.descrizione())  