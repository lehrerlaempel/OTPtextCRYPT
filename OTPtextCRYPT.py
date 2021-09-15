"""

OTPtextCRYPT

Ein Prjekt von Lehrer Lämpel
https://github.com/lehrerlaempel

Homeapge des Projekts:
https://lehrerlaempel.github.io/OTPtextCRYPT/

Lizenz: GNU/GPL v3

Stand: 15.09.2021

"""

logo = r'''
 ^ ^  OTPtextCRYPT
(O,O)         v4.0
(   )
-"-"--------------
'''

import secrets
import os
import pickle
import time

utabelle = {
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17,
    "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25,
    "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32,
    "X": 33, "Y": 34, "Z": 35, "Ä": 36, "Ö": 37, "Ü": 38,
    
    "a": 39, "b": 40, "c": 41, "d": 42, "e": 43, "f": 44, "g": 45, "h": 46,
    "i": 47, "j": 48, "k": 49, "l": 50, "m": 51, "n": 52, "o": 53, "p": 54,
    "q": 55, "r": 56, "s": 57, "t": 58, "u": 59, "v": 60, "w": 61,
    "x": 62, "y": 63, "z": 64, "ä": 65, "ö": 66, "ü": 67, "ß":68,
    
    " ": 69, ".": 70, ",": 71, ";": 72, ":": 73, "(": 74, ")": 75, "@": 76,
    "€": 77, "\"": 78, "'": 79, "!": 80, "&": 81, "/": 82, "\\": 83,
    "+": 84, "-": 85, "*": 86, "#": 87, "?": 88, "_": 89,
    
    "0": 90, "1": 91, "2": 92, "3": 93, "4": 94, "5": 95, "6": 96, "7": 97,
    "8": 98, "9": 99
    }


def wurmgenerator(num):
    """
    Erzeugt eine Liste aus Zufallszahlen der Länge "num".
    """
    wurm = []
    
    while len(wurm) < num:
        # Neuen Wert erzeugen
        randint = secrets.randbelow(10)

        # Einige werte verwerfen, den Rest zum Wurm hinzufügen
        if secrets.choice([True, False]):
            
            # zufällige Stelle im Wurm zum Einfügen auswählen
            variante = secrets.choice(["back", "front", "middle"])
            if variante == "back":
                pos = len(wurm)
            elif variante == "front":
                pos = 0
            else:
                pos = int(len(wurm) / 2)

            # Wert einfügen
            wurm.insert(pos, randint)
    
    return wurm


def wurmexport(wurmanzahl, wurmlaenge):
    """
    Erzeugt die gewünschte Anzahl Würdmer in der vorgegebenen Länge.
    Diese werden dann mit pickle als Liste binär "OTPtextCRYPT.db" gespeichert.
    """
    print()
    
    wuermer = []
    
    # Fortschritt ausgeben
    meilensteine = [int(wurmanzahl/b-1) for b in range(1,10)]
    prozentzahl = 10
    
    for i in range(wurmanzahl):
        wuermer.append(wurmgenerator(wurmlaenge))
        if i in meilensteine:
            print(f'{prozentzahl}%', end=' ')
            prozentzahl += 10
    
    with open('OTPtextCRYPT.db', 'wb') as datenbank:
        pickle.dump(wuermer, datenbank)
   
    print('Fertig!')
        
def wurmimport():
    '''
    Öffnet die Datei "OTPtextCRYPT.db".
    Gibt die ausgelesenen Würmer als Listenelemente zurück
    '''  
    wuermer = []
    
    with open('OTPtextCRYPT.db', 'rb') as datenbank:
        wuermer = pickle.load(datenbank)
        
        
    return wuermer


def klartext2numbers(klartext):
    """
    Setzt einen String gemäß Umsetztabelle in eine Liste von Ziffern um
    Was nicht in der Tabelle ist, wird gelöscht
    """
    doppelzahlliste = [utabelle[c] for c in klartext if c in utabelle]
    
    zahlenliste = []
    
    for gruppe in doppelzahlliste:
        gruppe = str(gruppe)
        for ziffer in gruppe:
            zahlenliste.append(int(ziffer))
            
    return zahlenliste

def numbers2klartext(einzelzahlenliste):
    """
    Setzt eine Liste aus Zahlen nach der Umsetztabelle
    in den ursprünglichen Klartext um.
    """
    doppelzahlenliste = []

    while len(einzelzahlenliste) > 1: # Größe 1 um einzelne Ziffern am Ende zu ignorieren
        neuezahl = ''.join(str(i) for i in einzelzahlenliste[:2])
        doppelzahlenliste.append(int(neuezahl))
        einzelzahlenliste = einzelzahlenliste[2:]
   
    klartextliste = []
    klartext = ''
    # Zahlen aus doppelzahlenliste nach Wörterbuch in Buchstaben umsetzen
    for zahl in doppelzahlenliste:
        buchstabe = [b for b, z in utabelle.items() if z == zahl]
        klartextliste.append(buchstabe[0])

    # Liste in String umwandeln
    klartext = ''.join(i for i in klartextliste)

    return klartext

        
def RandomWurmUndZuschnitt(notwendigeLaenge):
    """
    Wählt zufällig einen Wurm aus und passt die Länge an
    gibt die Wurmnummer als int zurück
    """
    wuermer = wurmimport()
    wurm = secrets.choice(wuermer)
    
    wurmnummer = wuermer.index(wurm)
    
    return wurm[:notwendigeLaenge], wurmnummer

def number2cypher(klarzahlen, keyzahlen, wurmnummer):
    """
    Verschlüsselt eine Liste klarzahlen der Liste keyzahlen
    Ausgabe: Cypher als String inkl. vorangestellte WurmID
    """

    # Zahlen (klarzahlen) vom Schlüssel (key) abziehen
    cypher = []
    for i in range(len(klarzahlen)):
        h = keyzahlen[i] - klarzahlen[i]
        # wenn Ergebnis < 0 dann plus 10 rechnen
        if h < 0:
            h += 10
        cypher.append(h)
        
    # Cypher zu String machen
    cypher_str = ''.join([str(i) for i in cypher])
    
    # Ermittlung der ID-Länge
    wuermer = wurmimport()
    id_laenge = str(len(wuermer))
    
    # ID auf maxlänge bringen
    wurmnummer = str(wurmnummer)
    while len(wurmnummer) < len(id_laenge):
        wurmnummer = '0'+wurmnummer
    
    chiffratInklID = wurmnummer + cypher_str

    return chiffratInklID

def cypher2number(cypher_string):
    '''
    Erwartet als Eingabe einen String.
    Gibt den Klartext als Ziffernfolge aus
    '''
    
    cypher_string = cypher_string.strip()
    
    # ID und wurm trennen
    wuermer = wurmimport()
    id_laenge = len(str(len(wuermer)))
    
    chiffrat = cypher_string[id_laenge:]
    ID = cypher_string[:id_laenge]
    
    # Schluessel auswählen
    key = wuermer[int(ID)]
    
    # Chiffrat in Liste
    cypher = [int(i) for i in chiffrat]

    numbers = []
    for i in range(len(cypher)):
        h = key[i] - cypher[i]
        if h < 0:
            h += 10
        numbers.append(h)
        
    return numbers

"""
                Ab hier dann die Programm-Logik
"""


def ErsterStartTest():
    """
    Prüft, ob eine Datenbank vorhanden ist.
    Wenn nicht, wird eine angelegt.
    """
    # Prüfen, ob DB angelegt ist
    if os.path.exists("OTPtextCRYPT.db") is False:
        print('Es wurde keine Datenbank gefunden!')
        
        wurmanzahl = int(input('Wie viele Würmer sollen erstellt werden?' +\
                               '\nNummer eingeben (mind. 1000): '))
        wurmlaenge = int(input('Wie lang sollen diese sein?\n' +\
                               'Nummer eingeben (mind. 1000): '))
        wurmexport(wurmanzahl, wurmlaenge)
        

def verschluesselung(klartext):
    '''
    Klartext zu Chiffrat
    Input wie Output ein String
    '''

    # print(klartext)
    
    inziffern = klartext2numbers(klartext)
    # print('Klartext', inziffern)
    
    key, keynummer = RandomWurmUndZuschnitt(len(inziffern))
    # print('key: ', key)
    # print('keynummer: ', keynummer)
    
    chiffrat = number2cypher(inziffern, key, keynummer)
    # print('Chiffrat: ', chiffrat)

    return chiffrat


def entschluesselung(chiffrat):
    '''
    Chiffrat zu Klartext
    Input wie Output ein String
    '''
    
    klartext_roh = cypher2number(chiffrat)
    # print('Klartext in Zahlen: ', klartext_roh)
    
    klartext = numbers2klartext(klartext_roh)
    #print('Klartext: ', klartext)

    return klartext


# # Test
# a = verschluesselung('Hallo, ich bin ein Test.')
# b = entschluesselung(a)

# print(a)
# print(b)

"""
                Ab hier die CLI-Version
"""

print()
print(logo)

time.sleep(1)

# StartUpRoutine
ErsterStartTest()

wahlmoeglichkeiten = '''Bitte wählen Sie aus folgenden Optionen:
    [1] Verschlüsselung
    [2] Entschlüsselung
    [3] Programm beenden

Ihre Auswahl: '''

nutzereingabe = 0

while nutzereingabe != 3:
    try:
        nutzereingabe = int(input(wahlmoeglichkeiten))
    except:
        nutzereingabe = 9
    
    # Verschlüsselung
    if nutzereingabe == 1:
        klartext = input('Bitte geben Sie den zu verschlüsselnden Text ein:\n')
        print('\nMoment, das kann kurz dauern...')
        chiffrat = verschluesselung(klartext)
        print(f'\nVerschlüsselt ergibt das:\n{chiffrat}')
        
        input('Enter drücken, um Fortzufahren...')
    
    # Entschlüsselung
    elif nutzereingabe == 2:
        chiffrat = input('Bitte geben Sie ein Chiffrat ein:\n')
        print('\nMoment, das kann kurz dauern...')
        klartext = entschluesselung(chiffrat)
        print(f'\nEntschlüsselt ergibt das:\n{klartext}')
        
        input('Enter drücken, um Fortzufahren...')    
    # Beenden
    elif nutzereingabe == 3:
        print('\nOTPtextCRYPT ist freie Software.\n' + \
              'Frei bezieht sich übrigens auf Freiheit, nicht (nur) auf den Preis.')
        print('\nDas Programm wird in 5 Sekunden beendet.\nAuf Wiedersehen!\n')
        time.sleep(5)
        break
    
    else:
        print('\nDas hat nicht geklappt.\nBitte wiederholen Sie Ihre Eingabe.')
        input('Enter drücken, um Fortzufahren...')
