class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita, categoria, attributo_specifico):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.categoria = categoria  # Specifica il tipo di prodotto
        self.attributo_specifico = attributo_specifico  # Attributo specifico per la categoria
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
   
class Elettronica:
    def crea_prodotto(nome, costo_produzione, prezzo_vendita, garanzia):
        return Prodotto(nome, costo_produzione, prezzo_vendita, "Elettronica", f"Garanzia: {garanzia} anni")

class Abbigliamento:
    def crea_prodotto(nome, costo_produzione, prezzo_vendita, materiale):
        return Prodotto(nome, costo_produzione, prezzo_vendita, "Abbigliamento", f"Materiale: {materiale}")

class Fabbrica:
    def __init__(self):
        self.inventario = {}
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantita"] += quantita
        else:
            self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantita": quantita}
        print(f"Aggiunti {quantita} pezzi di {prodotto.nome} all'inventario.")
        
    def vendi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario and self.inventario[nome_prodotto]["quantita"] >= quantita:
            self.inventario[nome_prodotto]["quantita"] -= quantita
            profitto = self.inventario[nome_prodotto]["prodotto"].calcola_profitto() * quantita
            print(f"Venduti {quantita} pezzi di {nome_prodotto}. Profitto totale: {profitto}")
            if self.inventario[nome_prodotto]["quantita"] == 0:
                del self.inventario[nome_prodotto]
        else:
            print("Prodotto non disponibile o quantità insufficiente.")
    
    def resi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]["quantita"] += quantita
            print(f"Restituiti {quantita} pezzi di {nome_prodotto} all'inventario.")
        else:
            print("Prodotto non presente in inventario.")  