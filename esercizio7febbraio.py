class Veicolo:
    def __init__(self, marca, modello, anno): 
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False #il veicolo è spento di default, booleano
        
    #getter per marca, modello, anno
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
        return self.__modello
    
    def get_anno(self):
        return self.__anno
    
    #Getter e setter per lo stato di accensione
    def accendi(self): #self permette di accedere ai suoi attributi
        self.__accensione = True #imposta l'accensione su true
        print(f"{self._marca} {self._modello} è stato acceso.") 

    def spegni(self):
        self.__accensione = False
        print(f"{self._marca} {self._modello} è stato spento.")

    def is_acceso(self):
        return self.__accensione

    def __str__(self):
        stato = "Acceso" if self.__accensione else "Spento"
        return f"{self._marca} {self.modello} ({self._anno}) - {stato}"
    
# Classe Furgone con incapsulamento
class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super()._init_(marca, modello, anno)
        self.__capacita_carico = capacita_carico #attributi privati
        self.__carico_attuale = 0  # Il furgone parte scarico

    def get_capacita_carico(self):
        return self.__capacita_carico
    
    def carica(self, peso):
        if self._carico_attuale + peso <= self._capacita_carico: #controlla se il peso totale dopo l'aggiunta rimarrebbe entro il peso massimo
            self.__carico_attuale += peso #somma il peso attuale piu il nuovo carico
            print(f"{self.get_marca()} {self.get_modello()} ha caricato {peso}kg. Totale: {self.__carico_attuale}kg.")
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Carico eccessivo! Capacità massima {self.__capacita_carico}kg.")

    def scarica(self, peso):
        if self.__carico_attuale - peso >= 0: #verifica che il carico attuale non diventi negativo dopo la rimozione
            self.__carico_attuale -= peso #sottrae il peso scaricato
            print(f"{self.get_marca()} {self.get_modello()} ha scaricato {peso}kg. Rimangono: {self.__carico_attuale}kg.") #mostra il nuovo peso dopo la rimozione
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Non puoi scaricare più di quello che hai caricato!") #se si prova a scaricare piu peso di quello presente, viene mostrato un errore
            
# Classe Motocicletta con incapsulamento
class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super()._init_(marca, modello, anno)
        self.__tipo = tipo  # attributo privato con l'incapsulamento, ad esempio sportiva, touring, custom

    def get_tipo(self):
        return self.__tipo

    def esegui_wheelie(self):
        if self.__tipo.lower() == "sportiva": #conversione in minuscolo
            print(f"{self.get_marca()} {self.get_modello()} esegue un wheelie!")
        else:
            print(f"{self.get_marca()} {self.get_modello()}: Questo tipo di moto non è adatto per i wheelie.")
            
# Classe GestoreParcoVeicoli con incapsulamento
class GestoreParcoVeicoli: #non eredita, classe indipendente
    def __init__(self):
        self.__veicoli = [] #attributo privato con lista vuota

    def aggiungi_veicolo(self, veicolo): #metodo pubblico
        self.__veicoli.append(veicolo)
        print(f"Veicolo {veicolo.get_marca()} {veicolo.get_modello()} aggiunto al parco.") #marca e modello sono privati quindi utilizziamo i get

    def rimuovi_veicolo(self, marca, modello):
        for veicolo in self.__veicoli: #uso il ciclo for per scorrere i veicoli dalla lista
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello: #se marca e modello corrispondono ad un veicolo presente
                self.__veicoli.remove(veicolo) # lo rimuove
                print(f"Veicolo {marca} {modello} rimosso dal parco.")
                return #messaggio di conferma
        print(f"Nessun veicolo {marca} {modello} trovato nel parco.")

    def lista_veicoli(self):
        if not self.__veicoli: #controlla se la lista è vuota
            print("Il parco veicoli è vuoto.")
        else:
            print("Veicoli nel parco:") #altrimenti stampa i veicoli presenti
            for veicolo in self.__veicoli: #ciclo for per stampare i veicoli presenti nel parco
                print(f"- {veicolo}") #stampa direttamente l'oggetto veicolo
                


        
 