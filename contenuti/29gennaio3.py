# Definisci la lista di numeri
numeri = [3, 7, 2, 9, 4, 10, 6]

# Controlla se la lista è vuota
if not numeri:
    print("Lista Vuota")
else:
    # Trova il numero massimo utilizzando un ciclo for
    max_numero = numeri[0]
    for numero in numeri:
        if numero > max_numero:
            max_numero = numero
    
    # Conta il numero di elementi nella lista utilizzando un ciclo while
    conteggio = 0
    indice = 0
    while indice < len(numeri):
        conteggio += 1
        indice += 1
    
    # Stampa i risultati
    print(f"Numero massimo: {max_numero}")
    print(f"Numero di elementi nella lista: {conteggio}")

