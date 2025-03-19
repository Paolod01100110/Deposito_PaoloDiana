import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

wine = load_wine()
X = wine.data
y = wine.target

# standardizzazione
scaler = StandardScaler() #standardizza le variabili per avere media 0 e varianza 1
X_scaled = scaler.fit_transform(X) #calcolo media e dev stnd

# suddividisione i dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#  algoritmo di classificazione
classifier = DecisionTreeClassifier(random_state=42) #inizializzo il classificatore basato sull'albero decisioonale
classifier.fit(X_train, y_train) #addestro il modello
y_pred = classifier.predict(X_test) #predizione

# 5. Valuta la performance del modello
report = classification_report(y_test, y_pred, output_dict=True) #metriche di valutazione, report in formato dizionario
report_df = pd.DataFrame(report).transpose() #conversione del report in dataframe per la visualizzazione tabellare
print(report_df)

# 6. Visualizza la matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred) #calcolo la matrice di confusione

# Visualizza la matrice di confusione
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d",
            xticklabels=wine.target_names, yticklabels=wine.target_names) #etichetta gli assi con il nome delle classi
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

