import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42) #generatore numeri casuali
giorni = np.arange(305) #generatore array di numeri interi 305 giorni
visitatori_medi = 1200
deviazione_std = 900

dati_visite = np.random.normal(loc=visitatori_medi, scale=deviazione_std, size=305) #genera 305 numeri casuali seguendo una distribuzione normale

trend_decrescente = np.linspace(0, 500, 305) #genera 305 valori equidistanti tra 0 e 500
dati_visite = dati_visite - trend_decrescente #sottraggo il trend decrescente, in tal modo il numeri di visitatori diminuisce gradualmente nel tempo

dati_visite = np.maximum(dati_visite, 0) #assicura che il numero di visitatori non sia negativo, ma almeno pari a zero

patologie = np.random.choice(['ossa', 'cuore', 'testa'], size=305) #creo una colonna casuale per patologia, assegna casualmente una delle tre patologie ad ogni giorno

df = pd.DataFrame({'Visitatori': dati_visite, 'Patologia': patologie}, index=giorni) #creazione del dataframe con le colonne visitatori e patologie e come indice i giorni

df['Mese'] = pd.to_datetime(df.index).to_period('M') #conversione delle date giornaliere in mesi
analisi_mensile = df.groupby('Mese')['Visitatori'].agg(['mean', 'std']) #seleziono la colonna visitarori e calcolo mean e std
print("Media e deviazione standard dei visitatori per mese:")
print(analisi_mensile)

patologie_counts = df['Patologia'].value_counts() #seleziona la colonna delle patologie e le conta
print(patologie_counts)

patologia_piu_comune = patologie_counts.idxmax()
print(patologia_piu_comune)

patologia_meno_comune = patologie_counts.idxmin()
print(patologia_meno_comune)

df['Media Mobile (7 giorni)'] = df['Visitatori'].rolling(window=7).mean() #calcolo della media mobile a 7 giorni
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri', color='blue', alpha=0.6)
plt.plot(df.index, df['Media Mobile (7 giorni)'], label='Media Mobile (7 giorni)', color='red', linewidth=2)
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.title('Numero di Visitatori Giornalieri in un Ospedale con Media Mobile')
plt.legend()
plt.grid()
plt.show()


