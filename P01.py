# Initialisierung
geheimzahl = 8015
eingabe = 0
counter = 0

# Schleifenkopf und Schleifenkörper
while eingabe != geheimzahl:
    eingabe = int (input("Ganze Zahl eingeben: "))

    if eingabe < geheimzahl:
        print ("Zahl zu klein")

    if eingabe > geheimzahl:
        print("Zahl zu gross")

    counter += 1

print("Richtig Sie haben", counter, " Versuche benoetigt")