class Veicolo:
    def __init__(self, marca, modello, anno): 
        self.__marca = marca #definizione degli attributi privati di classe
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False  # Il veicolo è spento di default (booleano)
        
    # Getter per marca, modello, anno
    def get_marca(self): #il get permette di leggere gli attributi privati senza modificarli direttamente
        return self.__marca
    
    def get_modello(self):
        return self.__modello
    
    def get_anno(self):
        return self.__anno
    
    # Getter e setter per lo stato di accensione
    def accendi(self):
        self.__accensione = True #imposta accensione su true
        print(f"{self.__marca} {self.__modello} è stato acceso.")

    def spegni(self):
        self.__accensione = False
        print(f"{self.__marca} {self.__modello} è stato spento.")

    def is_acceso(self): #restuisce lo stato di accensione
        return self.__accensione

    def __str__(self):
        stato = "Acceso" if self.__accensione else "Spento"
        return f"{self.__marca} {self.__modello} ({self.__anno}) - {stato}" #concatenazione con stato, cioè aggiunge lo stato acceso o spento alla fine della stringa
    
# Classe Auto
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_posti):
        super().__init__(marca, modello, anno)
        self.__numero_posti = numero_posti #attributo privato e specifico per la classe auto
    
    def get_numero_posti(self): #restituisce numero posti
        return self.__numero_posti
    
    def suona_clacson(self):
        print(f"{self.get_marca()} {self.get_modello()} fa 'Beep Beep!'") #uso di get invece di accedere direttamente agli attributi privati

# Classe Furgone
class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super().__init__(marca, modello, anno)
        self.__capacita_carico = capacita_carico #attributo privato per capacità massima di carico
        self.__carico_attuale = 0 #attributo privato per capacità attuale

    def get_capacita_carico(self): #restituisce la capacità di carico del furgone
        return self.__capacita_carico
    
    def carica(self, peso): #peso, quantità di carico da aggiungere
        if self.__carico_attuale + peso <= self.__capacita_carico: #la condizione if controlla se il peso totale dopo l'aggiunta rimane entro il limite massimo
            self.__carico_attuale += peso #somma il carico attuale al nuovo peso
            print(f"{self.get_marca()} {self.get_modello()} ha caricato {peso}kg. Totale: {self.__carico_attuale}kg.")
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Carico eccessivo! Capacità massima {self.__capacita_carico}kg.")

    def scarica(self, peso):
        if self.__carico_attuale - peso >= 0: #verifica che il carico attuale non diventa negativo dopo la rimozione
            self.__carico_attuale -= peso #sottrae il peso scaricato
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
        self.__veicoli = [] #inizializza un attributo privato contenente una lista vuota per memorizzare i veicoli

    def aggiungi_veicolo(self, veicolo):
        self.__veicoli.append(veicolo)
        print(f"Veicolo {veicolo.get_marca()} {veicolo.get_modello()} aggiunto al parco.")

    def rimuovi_veicolo(self, marca, modello):
        for veicolo in self.__veicoli: #ciclo for per scorrere tutti i veicoli presenti
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello: #se marca e modello corrispondono ad un veicolo presente nella lista, lo rimuove
                self.__veicoli.remove(veicolo)
                print(f"Veicolo {marca} {modello} rimosso dal parco.")
                return #il metodo termina evitando ricerche inutili
        print(f"Nessun veicolo {marca} {modello} trovato nel parco.")

    def lista_veicoli(self): #metodo pubblico che mostra i veicoli presenti al parco
        if not self.__veicoli: #controlla se la lista è vuota
            print("Il parco veicoli è vuoto.")
        else:
            print("Veicoli nel parco:")
            for veicolo in self.__veicoli: #ciclo for per stampare tutti i veicoli nel parco
                print(f"- {veicolo}") #stampa direttamente l'oggetto del veicolo
                
# Esempio di utilizzo
if __name__ == "__main__": #il codice viene eseguito solo se il file viene eseguito direttamente, senza import
    gestore = GestoreParcoVeicoli() #istanza della classe

    # Creazione veicoli
    auto1 = Auto("Fiat", "Panda", 2020, 5)
    furgone1 = Furgone("Ford", "Transit", 2018, 1000)
    moto1 = Motocicletta("Yamaha", "R1", 2022, "sportiva")

    # Aggiunta al parco veicoli
    gestore.aggiungi_veicolo(auto1)
    gestore.aggiungi_veicolo(furgone1)
    gestore.aggiungi_veicolo(moto1)

    # Mostra veicoli
    gestore.lista_veicoli() #mostra l'elenco dei veicoli

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
