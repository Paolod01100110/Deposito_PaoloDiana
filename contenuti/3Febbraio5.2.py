class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False  # Il ristorante è chiuso di default
        self.menu_piatti = []  # Lista dei nomi dei piatti
        self.menu_prezzi = []  # Lista dei prezzi corrispondenti ai piatti

    def descrivi_ristorante(self):
        print(f"\nIl ristorante '{self.nome}' offre cucina {self.tipo_cucina}.")

    def stato_apertura(self):
        stato = "APERTO"
        if self.aperto == False:
            stato = "CHIUSO"
        print(f"\nIl ristorante '{self.nome}' è attualmente {stato}.")

    def apri_ristorante(self):
        if self.aperto == True:
            print(f"\nIl ristorante '{self.nome}' è già aperto.")
            return
        
        self.aperto = True
        print(f"\nIl ristorante '{self.nome}' è ora APERTO!")

    def chiudi_ristorante(self):
        if self.aperto == False:
            print(f"\nIl ristorante '{self.nome}' è già chiuso.")
            return
        
        self.aperto = False
        print(f"\nIl ristorante '{self.nome}' è ora CHIUSO.")

    def aggiungi_al_menu(self, piatto, prezzo):
        if piatto in self.menu_piatti:
            print(f"\nIl piatto '{piatto}' è già presente nel menu.")
            return
        
        self.menu_piatti.append(piatto)
        self.menu_prezzi.append(prezzo)
        print(f"\nPiatto '{piatto}' aggiunto al menu con prezzo {prezzo:.2f}€.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu_piatti:
            indice = self.menu_piatti.index(piatto)
            self.menu_piatti.pop(indice)
            self.menu_prezzi.pop(indice)
            print(f"\nPiatto '{piatto}' rimosso dal menu.")
            return
        
        print(f"\nIl piatto '{piatto}' non è presente nel menu.")

    def stampa_menu(self):
        if len(self.menu_piatti) > 0:
            print("\nMenu del ristorante:")
            for piatto, prezzo in zip(self.menu_piatti, self.menu_prezzi):
                print(f"- {piatto}: {prezzo:.2f}€")
            return
        
        print(f"\nIl menu di '{self.nome}' è ancora vuoto!")

# --- Esempio di utilizzo ---
ristorante = Ristorante("La Buona Tavola", "Italiana")
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.stato_apertura()
ristorante.aggiungi_al_menu("Pasta alla Carbonara", 12.50)
ristorante.aggiungi_al_menu("Pizza Margherita", 8.00)
ristorante.aggiungi_al_menu("Tiramisù", 5.50)
ristorante.stampa_menu()
ristorante.togli_dal_menu("Pizza Margherita")
ristorante.stampa_menu()
ristorante.chiudi_ristorante()
ristorante.stato_apertura()
