class Persona:
    def __init__(self, nome: str, eta: int):
        self.__nome = nome  # Attributo privato
        self.__eta = eta    # Attributo privato
        
    # Getter per nome
    def get_nome(self):
        return self.__nome
    
    # Setter per nome
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome
    
    # Getter per età
    def get_eta(self):
        return self.__eta
    
    # Setter per età
    def set_eta(self, nuova_eta):
        if nuova_eta > 0:
            self.__eta = nuova_eta
        else:

         print("Errore: L'età deve essere un numero positivo.")
    
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.__nome} e ho {self.__eta} anni.")
        
class Studente(Persona):
    def __init__(self, nome: str, eta: int, voti: list):
        super().__init__(nome, eta)
        self.voti = voti  # Lista di voti
    
    def calcola_media(self):
        if self.voti:
            return sum(self.voti) / len(self.voti)
        return 0
    
    def presentazione(self):
        media = self.calcola_media()
        print(f"Ciao, mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. La mia media voti è {media:.2f}.")
        
class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__(nome, eta)
        self.materia = materia  # Materia insegnata
    
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. Insegno {self.materia}.")


# Esempio d'uso
studente1 = Studente("Marco Rossi", 17, [8, 9, 7, 6])
studente1.presentazione()

professore1 = Professore("Laura Bianchi", 45, "Matematica")
professore1.presentazione()