# import modul
import random

# Initialisierung
versuche = 3
geheimzahl = 8015
eingabe = 0
counter = 0
count_versuche = 0

# Schleifenkopf und Schleifenkörper
while eingabe != geheimzahl:
    eingabe = int (input("Ganze Zahl eingeben: "))

    if eingabe < geheimzahl:
        print ("Zahl zu klein")

    if eingabe > geheimzahl:
        print("Zahl zu gross")

    counter += 1
    count_versuche +=1

    if count_versuche == versuche:
        break

if eingabe == geheimzahl:
    print("Richtig Sie haben", counter, " Versuche benoetigt")
else:
    print("Sie haben die Zahl leider nicht erraten!")