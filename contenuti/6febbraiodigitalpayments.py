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
    
class BonificoBancario(MetodoPagamento):
    def __init__(self, nome, iban, saldo):
        super().__init__(nome, saldo)
        self.iban = iban
    
    def effettua_pagamento(self, importo):
        if importo > self._MetodoPagamento__saldo:
            return "Fondi insufficienti."
        self._MetodoPagamento__saldo -= importo
        return f"Pagamento di {importo}€ effettuato tramite bonifico bancario all'IBAN {self.iban}."

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def paga(self, importo):
        return self.metodo_pagamento.effettua_pagamento(importo)
    
# Esempio di utilizzo:
carta = CartaDiCredito("Carta Visa", "1234-5678-9012-3456", 500)
paypal = PayPal("Account PayPal", "marco@example.com", 300)
bonifico = BonificoBancario("Bonifico", "IT60X0542811101000000123456", 1000)

gestore = GestorePagamenti(carta)
print(gestore.paga(100))

gestore = GestorePagamenti(paypal)
print(gestore.paga(50))

gestore = GestorePagamenti(bonifico)
print(gestore.paga(200))
