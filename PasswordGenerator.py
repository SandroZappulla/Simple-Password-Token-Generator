# Password Generator 
# Author: Sandro Zappulla
# Github: @SandroZappulla
# version: v1.0

import secrets
import string

# Listen indem die Daten gespeichert werden
pw_data = []
token_data = []

# Programm starten
choice = 0
rtzrtztr

# Auswahlmöglichkeiten #
while choice == 0:
    print("PassGen v1.0 Sandro Zappulla")
    print("1. Passwörter")
    print("2. Tokens")
    #print("3. Listen Anzeigen")
    print("3. als .txt Speichern")
    print("4. Programm beenden")
    choice = int(input("Was wollen Sie generieren: \n"))

    # Passwörter Generieren
    if choice == 1:
        counter = 0
        # Zeichen die verwendet werden sollen
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
        amount_pw = int(input("Geben Sie an wie viele Passwörter Sie generieren möchten: \n"))
        length_pw = int(input("Bitte geben Sie die Länge des Passworts an: \n"))
        
        while counter < amount_pw:
            gen_pw = ''.join(secrets.choice(chars) for _ in range(length_pw))
            print(gen_pw)
            pw_data.append(gen_pw)
            counter +=1
        
        choice = 0

# Token generieren
    if choice == 2:
        counter = 0
        amount_token = int(input("Geben Sie an wie viele Tokens Sie generieren möchten: \n"))
        length_token = int(input("Bitte geben Sie die Länge des Tokens an: \n"))
        
        while counter < amount_token:
            gen_token = secrets.token_urlsafe(length_token)
            print(gen_token)
            token_data.append(gen_token)
            counter +=1
    
        choice = 0

    #if choice == 3:
    #    print(f"Die Daten für die Passwörter sind hier \n]{pw_data}")
    #    print(f"Die Daten für die Tokens sind hier \n]{token_data}")
            
    if choice == 3:
        # Speichern der Daten
        file_name = str(input("Wie soll die Datei heißen? \n"))
        # Datei erstellen
        alldata = open(f"{file_name}.txt", "a")

        #Passwörter aus der Liste in die Datei Schreiben
        alldata.write("Die Passwörter Lauten:\n")
        for anypw in pw_data:
            alldata.write(str(f"- {anypw}\n"))

        #Tokens aus der Liste in die Datei Schreiben
        alldata.write("Die Tokens Lauten:\n")
        for anytoken in token_data:
            alldata.write(str(f"- {anytoken}\n"))

        # Datei schließen
        alldata.close()

    # Programm beenden
    if choice == 4:
        print("Program wird Beendet...")
        quit()




