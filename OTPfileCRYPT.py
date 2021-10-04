# -*- coding: utf-8 -*-

"""
OTPfileCRYPT

Ein Prjekt von Lehrer Lämpel
https://github.com/lehrerlaempel

Lizenz: GNU/GPL v3

Stand: 04.10.2021
"""

logo = r'''
     .---.        .---------------
     /     \  __  /  OTPfileCRYPT
    / /     \(  )/  -----------
   //////   ' \/ ` ----------
  //// / // :    :     v1.0
 // /   /  /`    '-----     
//          //..\\
       ====UU====UU====
           '//||\\`
             ''``
'''

import time
import os
import pickle
import secrets
import OTPtextCRYPT as crypt

def ordner_anlegen():
    ordner = ['encrypt', 'decrypt']
    for i in ordner:
        if not os.path.exists(i):
            os.makedirs(i)

        
def files_verschluesseln():
    alledaten = os.listdir('encrypt')
    dateiliste = []
    for datei in alledaten:
        if datei[-4:] == '.txt':
            dateiliste.append(datei)
        
    for datei in dateiliste:
        
        print(f'\n"{datei}" wird verschlüsselt...')
        
        dateiname = 'encrypt/' + datei
        with open(dateiname, 'r', encoding=('utf-8')) as file:
            zeilen = file.readlines()
        
        cryptotozeilen = []
        for i in zeilen:
            chiffrat = crypt.verschluesselung(i)
            cryptotozeilen.append(chiffrat)
                                  
        dateiname_neu = 'encrypt/' + crypt.verschluesselung(datei) + '.OTPfileCRYPT'
        with open(dateiname_neu, 'wb') as output:
            pickle.dump(cryptotozeilen, output)
    
def files_entschluesseln():
    alledaten = os.listdir('decrypt')
    dateiliste = []
    for datei in alledaten:
        if datei[-13:] == '.OTPfileCRYPT':
            dateiliste.append(datei)
        
    for datei in dateiliste:
        
        print(f'\n"{datei}" wird entschlüsselt...')
        
        dateiname = 'decrypt/' + datei
        with open(dateiname, 'rb') as file:
            zeilen = pickle.load(file)
        
        klartext = []
        for i in zeilen:
            klar = crypt.entschluesselung(i)
            klartext.append(klar)
            
        dateiname_neu = 'decrypt/'+ crypt.entschluesselung(datei[:-13])

        for i in klartext:
            with open(dateiname_neu, 'a', encoding='utf-8') as output:
                output.write(str(i))
                output.write('\n')
    

if __name__ == '__main__':
    
    print(logo)

    ordner_anlegen()
    crypt.cli_programmstart()
    
    files_verschluesseln()
    files_entschluesseln()

    input('\nFertig.\nProgramm wird in 5 Sekunden beendet.')
    time.sleep(5)
