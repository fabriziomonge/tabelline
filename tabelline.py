# -*- coding: utf-8 -*-
"""Tabelline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sIqtvpEo504HkBXACV9f0g2DRm-4PULm
"""

import random
import pandas as pd
import time


D = 0
lista1=[]
lista2=[]
lista3=[]
lista4=[]

import streamlit as st


for i in range (100):
    if D != "fine":
        A = (random.randint(2,9))
        B = (random.randint(2,9))
        C = A*B
        testo = ("calcola "+str(A )+" X "+str(B)+ " =")
        D = st.text_input(testo,value="")
        if D == "":
            time.sleep(10)
    
    
    
        try:
            D = int(D)
        except:
            D = D
        
        if D == C:
            st.write("Risultato esatto, bravo")
        else:
            st.write("Errore, il risultato è:", C)
            
        lista1.append(A)
        lista2.append(B)
        lista3.append(C)
        lista4.append(D)
    
    else:
    i = 100

risultati = pd.DataFrame(lista1, columns=['moltiplicando'])
risultati['moltiplicatore'] = lista2
risultati['soluzione']=lista3
risultati['risposta di Pietro']=lista4

risultati

# risultati = risultati.head(len(risultati)-1)

# risultati['corr']=risultati.Pietro-risultati.soluzione

# importati = pd.read_excel('test_pietro.xlsx')
# importati = importati.set_index('Unnamed: 0',1)

# risultati_totali = importati.append(risultati)
# risultati_totali = risultati_totali.reset_index(drop=True)



# risultati.loc[risultati['corr']==0,'esatto']=1
# risultati = risultati.fillna(0)

# risultati_totali.loc[risultati_totali['corr']==0,'esatto']=1
# risultati_totali = risultati_totali.fillna(0)

# risultati_totali['numero'] = risultati_totali.index
# risultati_totali['bravura'] = risultati_totali.esatto.cumsum() / (risultati_totali.numero+1)

# risultati_totali.to_excel('test_pietro.xlsx')

# #per output
# numero_operazioni = len(risultati)
# numero_operazioni_tot = len(risultati_totali)

# corrette = risultati.esatto.sum()
# corrette_tot = risultati_totali.esatto.sum()


# print("")
# print("")
# print("In questa sessione hai effettuato", numero_operazioni, " operazioni, di cui ", corrette, " corrette")
# print("")
# print("Nella tua storia hai effettuato", numero_operazioni_tot, " operazioni, di cui ", corrette_tot, " corrette")
# print("")
# print("Eccole tue operazioni:")

# print(risultati_totali.drop('numero',1))

# risultati_totali.esatto.plot(kind = 'bar', figsize=(10,5))
# risultati_totali.bravura.plot(legend=True, color='r', figsize=(10,5))
