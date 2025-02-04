class Processore:
    def __init__(self, marca, velocita):
        self.marca = marca
        self.velocita = velocita  # in GHz
    
    def descrizione_processore(self):
        return f"Processore: {self.marca}, {self.velocita} GHz"

class Ram:
    def __init__(self, capacita):
        self.capacita = capacita  # in GB
    
    def descrizione_ram(self):
        return f"RAM: {self.capacita} GB"

class Computer(Processore, Ram):
    def __init__(self, marca_processore, velocita_processore, capacita_ram, marca):
        Processore.__init__(self, marca_processore, velocita_processore)
        Ram.__init__(self, capacita_ram)
        self.marca = marca
    
    def descrizione_computer(self):
        return f"Computer {self.marca} con {self.descrizione_processore()} e {self.descrizione_ram()}"

# Creazione di un oggetto Computer
pc = Computer("Intel", 3.5, 16, "Dell")
print(pc.descrizione_computer())
