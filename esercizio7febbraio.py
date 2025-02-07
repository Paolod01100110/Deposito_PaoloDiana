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
    
        
 