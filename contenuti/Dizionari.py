# Richiesta dell'input all'utente
booleano_input = input("Inserisci un valore booleano (True/False): ").strip().capitalize()
intero_input = int(input("Inserisci un numero intero: "))
stringa_input = input("Inserisci una stringa: ").strip()

# Conversione del valore booleano
if booleano_input == "True":
    booleano = True
else:
    booleano = False

# Creazione della lista con i dati
lista_dati = [booleano, intero_input, stringa_input]


