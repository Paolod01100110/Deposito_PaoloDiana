class ContoBancario:
    def __init__(self, titolare: str, saldo: float = 0.0): #titolare dovrebbe essere una stringa e il saldo un decimale
        self.__titolare = None  # Inizializzazione a none per passare attraverso il setter #attributi privati
        self.__saldo = saldo if saldo >= 0 else 0.0 #se saldo è maggiore di zero viene assegnato a self.__saldo, se negativo restituisce 0
        self.set_titolare(titolare)  # Usa il setter per la validazione, Invece di assegnare titolare direttamente, il valore passa attraverso set_titolare(), che applica una validazione.

    
    def get_titolare(self): #non permette la modifica da parte di un esterno
        return self.__titolare
    
    def set_titolare(self, nome):
        if isinstance(nome, str) and nome.strip(): #verifica che il nome sia una stringa e strip elimina eventuali spazi bianchi
            self.__titolare = nome.strip()
        else:
            raise ValueError("Il nome del titolare deve essere una stringa non vuota.")
    
    def deposita(self, importo: float):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo:.2f} effettuato. Saldo attuale: {self.__saldo:.2f}")
        else:
            print("Errore: L'importo da depositare deve essere positivo.")
    
    def preleva(self, importo: float):
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(f"Prelievo di {importo:.2f} effettuato. Saldo attuale: {self.__saldo:.2f}")
            else:
                print("Errore: Fondi insufficienti.")
        else:
            print("Errore: L'importo da prelevare deve essere positivo.")
    