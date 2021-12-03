# OTPtextCrypt v4.2
Simple vertrauenswürdige Textverschlüsselung

OTPtextCRYPT erstellt bei der ersten Verwendung zunächst eine einzigartige Datenbank mit vielen zufallsgenerierten Schlüsseln.

Diese können dann unter den Kommunikationspartnern ausgetauscht werden (indem man z.B. die Datenbank "OTPtextCRYPT.db einer Freundin auf einem USB-Stick übergibt).

Von da an können beide Seiten sicher miteinander kommunizieren, indem sie ihre Nachrichten mit dem Tool verschlüsseln. Wie diese dann übermittelt werden, ist egal: Man muss dem Weg schließlich nicht mehr vertrauen, da niemand das Chiffrat brechen kann, der nicht über den passenden Schlüssel verfügt.

## Vertrauenswürdig
Kennen Sie sogenannte [One-Time-Pads](https://de.wikipedia.org/wiki/One-Time-Pad), auch Einmalverschlüsselung genannt? Bei diesen ist mathematisch bewiesen, dass kein Angreifer das Chifrat brechen kann, egal über wie viel Rechenleistung er verfügt. Wir haben diese Handschlüssel-Methode aus dem kalten Krieg mit etwas Python ins 21. Jahrhundert katapultiert :-)

Andererseits ist das Programm [Freie Software](https://fsfe.org/freesoftware/freesoftware.de.html). Jede:r hat also die Möglichkeit, sich den Quelltext anzuschauen und nachzuvollziehen, wie das Programm genau funktioniert. 

...und da es ein recht simples Tool in der weit verbreiteten Sprache Python ist, hat man (anders als bei dem komplizierten Quelltext moderner OpenSource Crpyto-Messenger) auch als interessierter Laie eine realistische Chance, den Quelltext auch tatsächlich zu verstehen.

## Installationsanleitung
Sie müssen das Programm nicht installieren. Sie können einfach [hier](https://github.com/lehrerlaempel/OTPtextCRYPT/releases) die neuste Version von OTPtextCRYPT als PythonSkript hier herunterladen, entpacken und direkt ausführen.

Sollten Sie nicht wissen, wie Sie ein PythonSkript (*.py) ausführen können, finden Sie [hier](https://github.com/lehrerlaempel/pythonstarten) eine kurze Anleitung.

## Ein Beispiel
Alice und Bob sind Geschäftspartner, die gerne sicher kommunizieren möchten. Also läd sich Alice von dieser Seite OTPtextCrypt herunter, startet das Programm und lässt es einen neuen Satz Schlüssel erstellen. Diese speichert das Programm in einer Datenbank mit dem Namen "OTPtextCRYPT.db" in dem Ordner, in dem auch das Script gespeichert ist.

Alice kopiert das Skipt (OTPtextCRYPT.py) und die Datenbank auf einen USB-Stick und gibt diese beim nächsten Treffen Bob. Diser kopiert die Daten auf seinen PC. Nun können die beiden sicher kommunizieren in dem beruhigenden Wissen, dass niemand ihre Texte angreifen und entziffern kann - egal wie viel Rechenleistung und KnowHow der Angreifer investiert.

Zum Test verschlüsselt Bob direkt eine erste Nachricht:

`Ich bin ein geheimer Testtext.`

Das Programm erstellt daraus ein Chiffrat, das z.B. so aussehen könnte:

`78452119926177759572303716827013740498997374400590733193262543531`

Dieses schickt Bob nun an seine Freundin Alice. Per E-Mail, Messenger, Social Media, Postkarte, über die Kommentarspalte einer Webseite... egal, weil außer Alice das eh niemand entziffern kann.

Alice kopiert das erhaltene Chiffrat in ihr Tool und bekommt Bobs Nachricht angezeigt. 

## Datenschutz
OPTtextCRYPT erstellt eine lokale Datenbank mit Schlüsseln. Punkt. OPTtextCRYPT telefoniert nicht nach Hause und sammelt keine Daten. Es sendet und emfpängt auch keinerlei Daten über das Internet. Man kann die Software daher problemlos offline betreiben und die Chiffrate auf einem beliebigen Weg übermitteln: Übers Internet per Mail oder Messenger... oder auch von Hand mit Zitronensäuse auf ein Blatt Papier geschrieben.

## OTPfileCRYPT
In dem heruntergeladenen Archiv finden Sie neben dem oben beschriebenen OTPfileCRYPT auch eine zweite Datei mit dem Namen OTPfileCRYPT. Diese nutzt die Algorithmen von OTPtextCRYPT, verschlüsselt aber ganze Text-Dateien. Wenn man das Programm startet, legt es bei Bedarf eine Schlüsseldatenbank und die zwei Ordner `decrypt` sowie `encrypt` an. Von da an verschlüsselt es bei jedem Programmstart automatisch alle *.txt-Dateien im encrypt Ordner und entschlüsselt alle von OTPfileCRYPT verschlüsselten Daten aus dem Ordner decrypt. 

Und das beste: Auch die Dateinamen werden verschlüsselt :-)

Wer lange Beispiel-TXT-Daten zum Testen sucht, kann sich [hier](https://www.gutenberg.org/ebooks/2499.txt.utf-8) und [hier](https://www.gutenberg.org/ebooks/12108.txt.utf-8) deutsche Bücher als txt-File aus dem [Project Gutenberg](https://www.gutenberg.org/) herunterladen. (Funktioniert leider nicht mit einer deutschen IP-Adresse.)

## Anmerkung
Diese Software ist explizit nicht für den realen Einsatz bzw. die tatsächliche Übermittlung sensibler Informationen gedacht! 

Diese Software dient vielmehr dem Zweck, ein anschauliches und funktionierendes OTP-Beispiel zu geben, anhand dessen man zeigen kann, wieso wir theoretisch nicht-knackbare Verschlüsselung im IT-Alltag dann doch nicht verwenden.

## Freie Software
OTPtextCRYPT ist freie Software. Frei bezieht sich übrigens auf Freiheit, nicht (nur) auf den Preis.

Freie Software garantiert Ihnen die die vier grundlegenden Freiheiten, diese Software zu `verwenden`, zu `verstehen`, zu `verbreiten` und zu `verbessern`.

Mehr Infos zu freier Software finden Sie [hier](https://fsfe.org/freesoftware/freesoftware.de.html).

Sie können OTPtextCRYPT also unter den Bedingungen der von der Free Software Foundation veröffentlichten GNU General Public License (Version 3 der Lizenz) weiter verteilen und/oder modifizieren. 

OTPtextCRYPT wird in der Hoffnung bereitgestellt, dass es nützlich sein wird, jedoch OHNE JEDE GEWÄHR, sogar ohne die implizite Gewähr der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK. Siehe die GNU General Public License für weitere Einzelheiten. Eine Kopie der GNU General Public License finden Sie [hier](https://www.gnu.org/licenses/licenses.de.html).

## Danksagung
Danke an Jörg Drobick für [dessen faszinierende Website](http://scz.bplaced.net/), deren Unterseite zu [Manuelle Chiffrierverfahren](http://scz.bplaced.net/m.html) faszinierende Einblicke in die Geschichte klassischer Kryptoverfahren ermöglicht.
