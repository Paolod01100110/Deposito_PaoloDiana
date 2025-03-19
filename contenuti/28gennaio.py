# Credenziali hardcoded
username_corretta = "admin"
password_corretta = "12345"

# Input dell'utente
username = input("Inserisci il tuo nome utente: ")
password = input("Inserisci la tua password: ")

# Verifica delle credenziali
if username == username_corretta and password == password_corretta:
    print("Benvenuto, accesso effettuato con successo!")
else:
    print("Credenziali errate. Riprova.") 

    # Scelta della domanda segreta
    print("Ora puoi impostare una domanda segreta.")
    print("1. Qual è il tuo colore preferito?")
    print("2. Qual è il tuo animale preferito?")
    scelta = input("Scegli la domanda (1 o 2): ")

    if scelta == "1":
        risposta = input("Inserisci il tuo colore preferito: ")
        print(f"Hai impostato il tuo colore preferito come: (risposta")
    elif scelta == "2":
        risposta = input("Inserisci il tuo animale preferito: ")
        print(f"Hai impostato il tuo animale preferito come: {risposta}")
    else:
        print("Scelta non valida. Non è stata impostata alcuna domanda segreta.")