class MetodoPagamento:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo #attributo privato
    
    def effettua_pagamento(self, importo):
        if importo > self.__saldo:
            return "Fondi insufficienti."
        self.__saldo -= importo
        return "Metodo di pagamento non specificato."

class CartaDiCredito(MetodoPagamento):
    def __init__(self, nome, numero_carta, saldo):
        super().__init__(nome, saldo) #utilizzo di super per richiamare il costruttore della classe principale
        self.numero_carta = numero_carta
    
    def effettua_pagamento(self, importo):
        if importo > self._MetodoPagamento__saldo:
            return "Fondi insufficienti."
        self._MetodoPagamento__saldo -= importo
        return f"Pagamento di {importo}€ effettuato con carta di credito {self.numero_carta}."
    
class PayPal(MetodoPagamento):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, saldo)
        self.email = email
    
    def effettua_pagamento(self, importo):
        if importo > self._MetodoPagamento__saldo:
            return "Fondi insufficienti."
        self._MetodoPagamento__saldo -= importo
        return f"Pagamento di {importo}€ effettuato tramite PayPal all'email {self.email}."