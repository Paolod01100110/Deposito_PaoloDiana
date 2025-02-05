class Squadra: #questa classe è indipendente (nè padre, ne figlia), serve a raccogliere e a gestire i membri della squadra
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = []
        self.allenatori = []
        self.assistenti = []
    
    def aggiungi_giocatore(self, giocatore):
        self.giocatori.append(giocatore)
    
    def aggiungi_allenatore(self, allenatore):
        self.allenatori.append(allenatore)
    
    def aggiungi_assistente(self, assistente):
        self.assistenti.append(assistente)
    
    def descrivi_squadra(self):
        print(f"Squadra: {self.nome}")
        print("Giocatori:")
        for g in self.giocatori:
            g.descrivi()
        print("Allenatori:")
        for a in self.allenatori:
            a.descrivi()
        print("Assistenti:")
        for asst in self.assistenti:
            asst.descrivi()

class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni, è un membro della squadra.")

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni, è un giocatore nel ruolo di {self.ruolo} con la maglia numero {self.numero_maglia}.")
    
    def gioca_partita(self):
        print(f"{self.nome} sta giocando la partita come {self.ruolo} con il numero {self.numero_maglia}.")

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza
    
    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni, è l'allenatore con {self.anni_di_esperienza} anni di esperienza.")
    
    def dirige_allenamento(self):
        print(f"{self.nome} sta dirigendo un allenamento con la sua esperienza di {self.anni_di_esperienza} anni.")
        
class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
    
    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni, è un assistente specializzato in {self.specializzazione}.")
    
    def supporta_team(self):
        print(f"{self.nome} sta fornendo supporto alla squadra come {self.specializzazione}.")

# esempio di utilizzo e creazione oggetti:
squadra = Squadra("Inter FC")
giocatore = Giocatore("Marco Rossi", 25, "Attaccante", 9)
allenatore = Allenatore("Giovanni Bianchi", 45, 20)
assistente = Assistente("Luca Verdi", 35, "Fisioterapista")

#richiamo metodi della classe squadra
squadra.aggiungi_giocatore(giocatore)
squadra.aggiungi_allenatore(allenatore)
squadra.aggiungi_assistente(assistente)

#richiamo metodo descrivi squadra
squadra.descrivi_squadra()

#esecuzione metodi
giocatore.gioca_partita()
allenatore.dirige_allenamento()
assistente.supporta_team()