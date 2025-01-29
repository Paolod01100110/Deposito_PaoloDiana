# Conto alla rovescia con lista e ciclo while

while True:
    # Chiedi all'utente di inserire un numero
    numero = input("Inserisci un numero per iniziare il conto alla rovescia: ")

    # Verifica che l'input sia un numero valido
    if numero.isdigit():
        numero = int(numero)
        # Creazione della lista da 0 al numero inserito (ordine crescente)
        lista_numeri = list(range(0, numero + 1))

        print("Ecco i numeri della lista:")
        # Ciclo while per iterare sulla lista e stampare i numeri
        i = 0
        while i < len(lista_numeri):
            print(lista_numeri[i])
            i += 1

        # Chiedi all'utente se vuole ripetere
        ripeti = input("Vuoi ripetere il programma? (sì/no): ").strip().lower()
        if ripeti != "sì":
            print("Grazie per aver usato il programma. A presto!")
            break
    else:
        print("Per favore inserisci un numero valido.")