# Chiedi all'utente di inserire un numero
numero = input("Inserisci un numero: ")

# Verifica che l'input sia un numero valido
if numero.isdigit():
    numero = int(numero)
    
    # Controllo se il numero è pari o dispari
    if numero % 2 == 0:
        print("Pari")
    else:
        print("Dispari")
else:
    print("Per favore inserisci un numero valido.")