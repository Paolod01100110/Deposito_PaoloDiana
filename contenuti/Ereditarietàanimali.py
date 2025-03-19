class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self):
        print("L'animale emette un suono generico.")
    
    def descrizione(self):
        return f"Nome: {self.nome}, Età: {self.eta} anni"

# Classe Leone
class Leone(Animale):
    def __init__(self, nome, eta, forza):
        super().__init__(nome, eta)
        self.forza = forza
    
    def fai_suono(self):
        print("Il leone ruggisce: ROARRR!")
    
    def caccia(self):
        print(f"{self.nome} sta cacciando con una forza di {self.forza}.")

# Classe Giraffa
class Giraffa(Animale):
    def __init__(self, nome, eta, altezza):
        super().__init__(nome, eta)
        self.altezza = altezza
    
    def fai_suono(self):
        print("La giraffa emette un suono basso e gutturale.")
    
    def mangia_foglie(self):
        print(f"{self.nome} sta mangiando foglie dagli alberi con il suo collo lungo {self.altezza} metri.")

# Classe Pinguino
class Pinguino(Animale):
    def __init__(self, nome, eta, velocita_nuoto):
        super().__init__(nome, eta)
        self.velocita_nuoto = velocita_nuoto
    
    def fai_suono(self):
        

        print("Il pinguino fa un verso squillante: squawk!")
    
    def nuota(self):
        print(f"{self.nome} sta nuotando a una velocità di {self.velocita_nuoto} km/h.")

# Creazione di oggetti
leone = Leone("Simba", 5, 8)
giraffa = Giraffa("Melman", 10, 5.5)
pinguino = Pinguino("Pingu", 3, 15)


# Esempio di utilizzo degli oggetti
for animale in (leone, giraffa, pinguino):
    print(animale.descrizione())
    animale.fai_suono()


        
        