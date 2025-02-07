class Veicolo:
    def __init__(self, marca, modello, anno): 
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False  # Il veicolo è spento di default (booleano)
        
    # Getter per marca, modello, anno
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
        return self.__modello
    
    def get_anno(self):
        return self.__anno
    
    # Getter e setter per lo stato di accensione
    def accendi(self):
        self.__accensione = True
        print(f"{self.__marca} {self.__modello} è stato acceso.")

    def spegni(self):
        self.__accensione = False
        print(f"{self.__marca} {self.__modello} è stato spento.")

    def is_acceso(self):
        return self.__accensione

    def __str__(self):
        stato = "Acceso" if self.__accensione else "Spento"
        return f"{self.__marca} {self.__modello} ({self.__anno}) - {stato}"
    
# Classe Auto
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_posti):
        super().__init__(marca, modello, anno)
        self.__numero_posti = numero_posti
    
    def get_numero_posti(self):
        return self.__numero_posti
    
    def suona_clacson(self):
        print(f"{self.get_marca()} {self.get_modello()} fa 'Beep Beep!'")

# Classe Furgone
class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super().__init__(marca, modello, anno)
        self.__capacita_carico = capacita_carico
        self.__carico_attuale = 0

    def get_capacita_carico(self):
        return self.__capacita_carico
    
    def carica(self, peso):
        if self.__carico_attuale + peso <= self.__capacita_carico:
            self.__carico_attuale += peso
            print(f"{self.get_marca()} {self.get_modello()} ha caricato {peso}kg. Totale: {self.__carico_attuale}kg.")
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Carico eccessivo! Capacità massima {self.__capacita_carico}kg.")

    def scarica(self, peso):
        if self.__carico_attuale - peso >= 0:
            self.__carico_attuale -= peso
            print(f"{self.get_marca()} {self.get_modello()} ha scaricato {peso}kg. Rimangono: {self.__carico_attuale}kg.")
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Non puoi scaricare più di quello che hai caricato!")
            
# Classe Motocicletta
class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def esegui_wheelie(self):
        if self.__tipo.lower() == "sportiva":
            print(f"{self.get_marca()} {self.get_modello()} esegue un wheelie!")
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Questo tipo di moto non è adatto per i wheelie.")
            
# Classe GestoreParcoVeicoli
class GestoreParcoVeicoli:
    def __init__(self):
        self.__veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self.__veicoli.append(veicolo)
        print(f"Veicolo {veicolo.get_marca()} {veicolo.get_modello()} aggiunto al parco.")

    def rimuovi_veicolo(self, marca, modello):
        for veicolo in self.__veicoli:
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello:
                self.__veicoli.remove(veicolo)
                print(f"Veicolo {marca} {modello} rimosso dal parco.")
                return
        print(f"Nessun veicolo {marca} {modello} trovato nel parco.")

    def lista_veicoli(self):
        if not self.__veicoli:
            print("Il parco veicoli è vuoto.")
        else:
            print("Veicoli nel parco:")
            for veicolo in self.__veicoli:
                print(f"- {veicolo}")
                
# Esempio di utilizzo
if __name__ == "__main__":
    gestore = GestoreParcoVeicoli()

    # Creazione veicoli
    auto1 = Auto("Fiat", "Panda", 2020, 5)
    furgone1 = Furgone("Ford", "Transit", 2018, 1000)
    moto1 = Motocicletta("Yamaha", "R1", 2022, "sportiva")

    # Aggiunta al parco veicoli
    gestore.aggiungi_veicolo(auto1)
    gestore.aggiungi_veicolo(furgone1)
    gestore.aggiungi_veicolo(moto1)

    # Mostra veicoli
    gestore.lista_veicoli()

    # Accensione e spegnimento
    auto1.accendi()
    furgone1.spegni()

    # Azioni specifiche per tipo di veicolo
    auto1.suona_clacson()
    furgone1.carica(500)
    furgone1.scarica(200)
    moto1.esegui_wheelie()

    # Rimozione di un veicolo
    gestore.rimuovi_veicolo("Fiat", "Panda")

    # Mostra veicoli aggiornati
    gestore.lista_veicoli()
