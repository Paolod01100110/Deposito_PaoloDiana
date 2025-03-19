while True:
    # Chiedi all'utente di inserire un numero
    numero = input("Inserisci un numero intero positivo per iniziare il conto alla rovescia: ")

    # Verifica che l'input sia un numero intero positivo
    if numero.isdigit():
        numero = int(numero)
        
        # Ciclo while per stampare il conto alla rovescia
        for i in range(numero, -1, -1):
            print(i)

    else:
        print("Per favore inserisci un numero intero positivo valido.")