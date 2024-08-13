## IMPORT - BLOG

import random

#%% KLASSEN - BLOG

class Menschen():
    def __init__(self, name: str, sex: str, age: int, uni_stufe: int) -> None:
        self.name = name
        self.sex = sex
        self.age = age
        self.uni_stufe = uni_stufe
        self.hungry = 100
        self.thursty = 100
        self.health = 100
        self.money = 1000
        if self.sex == 'm':
            if self.name != 'Testing':        
                print(f'Der Spieler mit dem Namen {self.name} wurde erstellt.')
                print(f'Er verfügt aktuell über:')
        elif self.sex == 'w':   
            if self.name != 'Testing':     
                print(f'Die Spielerin mit dem Namen {self.name} wurde erstellt.')
                print(f'Sie verfügt aktuell über:')
        if self.name != 'Testing':
            print(f'{self.health}% Gesundheit')
            print(f'{self.hungry}% gesättigter Hunger')
            print(f'{self.thursty}% gestillter Durst')
            print(f'{self.money}€ Guthaben')
    def weniger_geld(self, wert: int|float):
        self.money -= wert
    def mehr_geld(self, wert: int|float):
        self.money += wert
    def weniger_healty(self, wert: int|float):
        self.health -= wert
    def mehr_healty(self, wert: int|float):
        self.health += wert
    def weniger_hungry(self, wert: int|float):
        self.hungry -= wert
    def mehr_hungry(self, wert: int|float):
        self.health += wert
    def weniger_thursty(self, wert: int|float):
        self.health -= wert
    def mehr_thursty(self, wert: int|float):
        self.health += wert
    def mehr_uni(self, uni_wert: int|float):
        self.uni_stufe += uni_wert
        print(f'Deine Universitätsstufe hat sich auf Stufe {self.uni_stufe} erhöht.')
    def anreise_urlaub(self)-> None:
        self.health -= 20
        self.hungry -= 20
        self.thursty -= 20
    def im_urlaub(self) -> None:
        print('Dein aktueller Spieler-Status:')
        print(f'{self.health}% Gesundheit')
        print(f'{self.hungry}% gesättigter Hunger')
        print(f'{self.thursty}% gestillter Durst')
        print(f'{self.money}€ Guthaben')

player1 = Menschen('Testing', 'm', 18, 0)

class Autos():
    def __init__(self, marke: str, modell: str, farbe: str) -> None:
        self.marke = marke
        self.modell = modell
        self.farbe = farbe
        self.fuel = 100
        self.damage = 100
        if self.marke != 'Testing':
            print(f'Das neue Fahrzeug {self.marke} {self.modell} in der Farbe {self.farbe} wurde erstellt.')
            print(f'Es verfügt aktuell über:')
            print(f'{self.fuel}% Tankfüllung')
            print(f'{self.damage}% Zustand')
            print(f'{player1.name} kann nun damit fahren.')
    def anreise_urlaub(self) -> None:
        self.fuel = 0
        self.damage -= 10
    def im_urlaub(self) -> None:
        print('Dein aktueller Fahrzeug-Status:')            
        print(f'{self.fuel}% Tankfüllung')
        print(f'{self.damage}% Zustand')
        
car1 = Autos('Testing', 'Test', 'Test')

class Staedte():
    def __init__(self, ortsname: str, einwohner: int, entfernung: int) -> None:
        self.ortsname = ortsname
        self.einwohner = einwohner
        self.entfernung = entfernung

class Haeuser():
    def __init__(self, ortsname: str, name:str, anzahl_zimmer: int, kosten: int|float) -> None:
        self.ortsname = ortsname
        self.name = name
        self.anzahl_zimmer = anzahl_zimmer
        self.kosten = kosten

class Berufe():
    def __init__(self, beruf: str, stunden: int, gehalt: int) -> None:
        self.beruf = beruf
        self.stunden = stunden
        self.gehalt= gehalt
        if self.beruf == 'Testing':
            pass
        else:
            print(f'Dein aktueller Beruf ist jetzt: {self.beruf}, Du arbeitest {self.stunden} Stunden und erhälst dafür {self.gehalt}€ pro Tag.')
    def arbeiten_ohne_travels(self) -> None:
        player1.health -= beruf.stunden * 5
        player1.thursty -= beruf.stunden * 5
        player1.hungry -= beruf.stunden * 5
        player1.money += beruf.gehalt
        print(f'Du hast {beruf.stunden} Stunden gearbeitet und:')
        print(f'{beruf.gehalt}€ verdient.')
        print(f'{beruf.stunden * 5} Gesundheit abgebaut')
        print(f'{beruf.stunden * 5} Durst abgebaut')
        print(f'{beruf.stunden * 5} Hunger abgebaut')
    def arbeiten_mit_travels(self) -> None:
        print(f'Du hast {beruf.stunden} Stunden gearbeitet und:')
        print('Es wurden kein Status abgebaut, weil Du noch Erholung vom Urlaub hast.')
    def beruf_anzeigen(self):
        print(f'Dein aktueller Beruf ist jetzt: {self.beruf}, Du arbeitest {self.stunden} Stunden und erhälst dafür {self.gehalt}€ pro Tag.')
        
beruf = Berufe('Testing', 1, 1)

#%% DEF - BLOG

def trenner():
    print('#####################################################################################')

def fahrprüfung():
    counter = 0
    while counter < 8:
        frage1 = input('Darf man Unfälle bauen ? ja / nein : ')
        if frage1.lower() == 'nein':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print()       
        frage2 = input('Muss man vorsichtig fahren ? ja / nein : ')
        if frage2.lower() == 'ja':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage3 = input('Muss man beim Auto fahren auch auf andere Autos achten ? ja / nein : ')
        if frage3.lower() == 'ja':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage4 = input('Darf man alle Verkehrsschilder ignorieren ? ja / nein : ')
        if frage4.lower() == 'nein':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage5 = input('Darf man immer nur so schnell fahren wie es erlaubt ist ? ja / nein : ')
        if frage5.lower() == 'ja':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage6 = input('Muss man nach einem Unfall die Polizei anrufen ? ja / nein : ')
        if frage6.lower() == 'ja':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage7 = input('Sollte man müde Auto fahren ? ja / nein : ')
        if frage7.lower() == 'nein':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage8 = input('Muss man für Benzin immer bezahlen an der Tankstelle ? ja / nein : ')
        if frage8.lower() == 'ja':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage9 = input('Muss man darauf achten das sein Auto stets repariert ist ? ja / nein : ')
        if frage9.lower() == 'ja':
            print('Super, das ist richtig! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        frage10 = input('Wirst Du ein guter Autofahrer sein ? ja / nein : ')
        if frage10.lower() == 'ja':
            print('Super, das ist sehr vorbildlich! Dafür gibt es einen Punkt')
            print()
            counter +=  1
        else:
            print('Leider war das nicht richtig! Dafür gibt es keinen Punkt')
            print() 
        
        if counter >= 8:
            print(f'Du hast {counter} Punkte erreicht und somit bestanden.')
        else:
            print(f'Du hast {counter} Punkte erreicht und somit nicht bestanden, die wurden 200€ für die Prüfung abgezogen und Du musst sie nun wiederholen!')
                    
        return player1.weniger_geld(200)
    
def spielauswahl():
    spielauswahl = random.randint(1, 4)
    if spielauswahl == 1:
        return spiel1()
    elif spielauswahl == 2:
        return spiel2()
    elif spielauswahl == 3:
        return spiel3()
    elif spielauswahl == 4:
        return spiel4()
    
def spiel1():
    
    while counter < 10:
        counter = 0
        runden = 0
        aufgabenauswahl = random.randint(1,5)
        if aufgabenauswahl == 1:
            tipp = 0
            runden += 1
            zahl1 = (random.randint(1, 101))
            zahl2 = (random.randint(1, 101))
            ergebnis = zahl1 + zahl2
            print(f'Was ist das Ergebnis aus {zahl1} + {zahl2} ? :')
            tipp = int(input('Ergebnis ?: '))
            if tipp == ergebnis:
                print('Klasse gerechnet, das Ergebnis ist richtig !!!\n')
                counter += 1
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')
            else:
                print(f'Leider nicht richtig, das Ergbnis ist {ergebnis}\n')
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')                
        elif aufgabenauswahl == 2:
            tipp = 0
            runden += 1
            zahl1 = (random.randint(1, 101))
            zahl2 = (random.randint(1, 101))
            ergebnis = zahl1 - zahl2
            print(f'Was ist das Ergebnis aus {zahl1} - {zahl2} ? :')
            tipp = int(input('Ergebnis ?: '))
            if tipp == ergebnis:
                print('Klasse gerechnet, das Ergebnis ist richtig !!!\n')
                counter += 1
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')
            else:
                print(f'Leider nicht richtig, das Ergbnis ist {ergebnis}\n')
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')
        elif aufgabenauswahl == 3:
            tipp = 0
            runden += 1
            zahl1 = (random.randint(1, 10))
            zahl2 = (random.randint(1, 10))
            ergebnis = zahl1 * zahl2
            print(f'Was ist das Ergebnis aus {zahl1} x {zahl2} ? :')
            tipp = int(input('Ergebnis ?: '))
            if tipp == ergebnis:
                print('Klasse gerechnet, das Ergebnis ist richtig !!!\n')
                counter += 1
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')
            else:
                print(f'Leider nicht richtig, das Ergbnis ist {ergebnis}\n')
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')
        elif aufgabenauswahl == 4:        
            tipp = 0
            runden += 1
            zahl1 = (random.randint(1, 101))
            zahl2 = (random.randint(1, 101))        
            while zahl1 % zahl2 != 0:
                zahl1 = (random.randint(1, 101))
                zahl2 = (random.randint(1, 101))
            ergebnis = zahl1 / zahl2    
            print(f'Was ist das Ergebnis aus {zahl1} : {zahl2} ? :')
            tipp = int(input('Ergebnis ?: '))
            if tipp == ergebnis:
                print('Klasse gerechnet, das Ergebnis ist richtig !!!\n')
                counter += 1
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')
            else:
                print(f'Leider nicht richtig, das Ergbnis ist {ergebnis}\n')
                print(f'Du hast bisher {counter} von {runden} Fragen richtig beantwortet, also {counter} Punkte erreicht !\n')

    print(f'\nSUPER GEMACHT !!! Du hast Feierabend und dafür {runden} Fragen benötigt')

def spiel2():
    
    secret_number = random.randint(1, 10)
    
    while versuch != 'gewonnen':
        count = 1
        versuch = ''
        print()
        print()        
        print("Ich habe mir soeben eine Zahl zwischen 1 und 10 ausgedacht.")
        print("Deine Aufgabe ist es nun, diese Zahl mit nur maximal 3 Versuchen herauszufinden.\n")
        print("Es dürfen nur ganze Zahlen zwischen 1 und 10 eingegeben werden.\n")

        try:
            zahl = int(input("Dein erster Versuch: "))
        except ValueError:
            print("ACHTUNG: Bitte hier nur die vorgegeben Zahlen 1 bis 10 eingeben\n\n")
            zahl = int(input("Dein erster Versuch: "))

        if zahl < 1 or zahl > 10:
            print("Es dürfen nur ganze Zahlen zwischen 1 und 10 eingegeben werden")
            zahl = int(input("Bitte erneut einen Versuch abgeben: "))
                
            print("\n")

        while count <= 3 and zahl != secret_number:
            if zahl < secret_number and zahl > 0:
                print("Deine eingegebene Zahl ist leider niedriger als die von mir gesuchte Zahl.")
                print("Das war dein " + str(count) + ". Versuch.\n")
                try:
                    zahl = int(input("Dein nächster Versuch: "))
                except ValueError:
                    print("ACHTUNG: Bitte hier nur die vorgegeben Zahlen 1 bis 50 eingeben\n\n")
                    zahl = int(input("Dein nächster Versuch: "))
                count += 1   
            elif zahl > secret_number and zahl < 51:
                print("Deine eingegebene Zahl ist leider größer als die von mir gesuchte Zahl.")
                print("Das war dein " + str(count) + ". Versuch.\n")
                try:
                    zahl = int(input("Dein nächster Versuch: "))
                except ValueError:
                    print("ACHTUNG: Bitte hier nur die vorgegeben Zahlen 1 bis 50 eingeben\n\n")
                    zahl = int(input("Dein nächster Versuch: "))
                count += 1
            else:
                print("Es dürfen nur ganze Zahlen zwischen 1 und 50 eingegeben werden")
                zahl = int(input("Bitte erneut einen Versuch abgeben: "))
        if zahl == secret_number:
            print("Herzlichen Glückwunsch, Du hast die von mir gesuchte Zahl erraten. Klasse Leistung !!!\n\n")
            versuch = 'gewonnen'
        else:
            print("Tut mir leid, Du hast die maximale Anzahl an Versuchen erreicht. Die gesuchte Zahl war: " + str(secret_number))
            print('Du musst es erneut versuchen')
            input('- Weiter mit beliebiger Taste -')
            print("\n\n")

def spiel3():
    versuch = ''
    while versuch != 'gewonnen':
        print()
        print()
        print("Dein Ziel ist es die Würfel vorauszusagen. Ich werde gleich einen Würfel mit den Zahlen 1 bis 6 würfeln.\n")
        print("Danach musst du schätzen ob der nächste Wurf:")
        print("( + ) Höher ausfällt")
        print("( - ) Niedriger ausfällt")
        print("( = ) Gleich ausfällt\n")
        print("Sollte von den 3 Versuchen, die Du hast, mindestens 2 Tipps korrekt sein, dann hast Du dieses Spiel gewonnen.\n")
        dices = [random.randint(1, 6) for i in range(4)]        
        count = 0
        round_count = 0        
        for i in range(4):
            print(f'Mein {i+1}. Wurf war eine {dices[round_count]}\n')            
            if round_count == 3:
                break            
            choice = input("Ist der nächste Wurf: Höher (+) oder Niedriger (-) oder Gleich (=) ? : ")
            if choice == "+" and dices[i + 1] > dices[i]:
                print("Klasse! Du hast einen richtigen Tipp abgegeben\n")                
                count += 1
                round_count += 1
            elif choice == "-" and dices[i + 1] < dices[i]:
                print("Klasse! Du hast einen richtigen Tipp abgegeben\n")
                count += 1
                round_count += 1
            elif choice == "=" and dices[i + 1] == dices[i]:
                print("Klasse! Du hast einen richtigen Tipp abgegeben\n")
                count += 1
                round_count += 1
            else:
                print("Leider war dein Tipp nicht richtig.")
                round_count += 1        
        if count > 1:
            print("Herzlichen Glückwunsch, Du hast " + str(count) + " Punkte erreicht und somit dieses Spiel gewonnen!")
            print()
            input('- Weiter mit beliebiger Taste -')
            versuch = 'gewonnen'
        else:
            print("Leider hast Du nur " + str(count) + " Punkt erreicht, vielleicht klappts beim nächsten Mal!")
            print('Du musst es nochmal probieren')
            input()
            input('- Weriter mit beliebiger Taste -')    
        print("\n\n")

def spiel4():
    print('Heute war der Chef nicht im Haus, ihr hattet Zeit euch unter den Kollegen einfach mal auszutauschen und es gab nichts weiter zu tun.')

def random_bonus(ort):
    money = random.randint(100, 500)
    player1.mehr_geld(money)
    print(f'Du hast während deiner Besichtigung der Sehenswürdigkeiten {ort} einen wohlhabenden Panda getroffen, er schenkt dir {money}€ und verschwindet wieder.')

#%% STANDARD - STÄDTE

london = Staedte('london', 8982000, 1170)
paris = Staedte('Paris', 2161000, 1159)
barcelona = Staedte(' Barcelona', 1620000, 1989)
wien = Staedte('Wien', 1897000, 927)
bern = Staedte('Bern', 133115, 1006)
warschau = Staedte('Warschau', 1765000, 613)
amsterdam = Staedte('Amsterdam', 821752, 684)
staedte = ['( 1 ) London', '( 2 ) Paris', '( 3 ) Barcelona', '( 4 ) Wien', '( 5 ) Bern', '( 6 ) Warschau', '( 7 ) Amsterdam']
#%% STANDARD - HÄUSER

### LONDON
hotel_london = Haeuser('London', 'Hotel', 100, 60 )
ferienwohnung_london = Haeuser('London', 'Ferienwohnung', 97, 40 )
restaurant_london = Haeuser('London', 'Restaurant', 1, 30 )
imbiss_london = Haeuser('London', 'Imbiss', 1, 20 )
kino_london = Haeuser('London', 'Kino', 10, 15 )
sights_london = Haeuser('London', 'Sehenswürdigkeiten', 10, 15 )
kiosk_london = Haeuser('London', 'Kiosk für Getränke', 1, 5 )
tankstelle_london = Haeuser('London', 'Tankstelle', 97, london.entfernung * 0.10 )
### PARIS
hotel_paris = Haeuser('Paris', 'Hotel', 100, 60 )
ferienwohnung_paris = Haeuser('Paris', 'Ferienwohnung', 97, 40 )
restaurant_paris = Haeuser('Paris', 'Restaurant', 1, 30 )
imbiss_paris = Haeuser('Paris', 'Imbiss', 1, 20 )
kino_paris = Haeuser('Paris', 'Kino', 10, 15 )
sights_paris = Haeuser('Paris', 'Sehenswürdigkeiten', 10, 15 )
kiosk_paris = Haeuser('Paris', 'Kiosk für Getränke', 1, 5 )
tankstelle_paris = Haeuser('Paris', 'Tankstelle', 97, paris.entfernung * 0.10 )
### BARCELONA
hotel_barcelona = Haeuser('Barcelona', 'Hotel', 100, 60 )
ferienwohnung_barcelona = Haeuser('Barcelona', 'Ferienwohnung', 97, 40 )
restaurant_barcelona = Haeuser('Barcelona', 'Restaurant', 1, 30 )
imbiss_barcelona = Haeuser('Barcelona', 'Imbiss', 1, 20 )
kino_barcelona = Haeuser('Barcelona', 'Kino', 10, 15 )
sights_barcelona = Haeuser('Barcelona', 'Sehenswürdigkeiten', 10, 15 )
kiosk_barcelona = Haeuser('Barcelona', 'Kiosk für Getränke', 1, 5 )
tankstelle_barcelona = Haeuser('Barcelona', 'Tankstelle', 97, barcelona.entfernung * 0.10 )
### WIEN
hotel_wien = Haeuser('Wien', 'Hotel', 100, 60 )
ferienwohnung_wien = Haeuser('Wien', 'Ferienwohnung', 97, 40 )
restaurant_wien = Haeuser('Wien', 'Restaurant', 1, 30 )
imbiss_wien = Haeuser('Wien', 'Imbiss', 1, 20 )
kino_wien = Haeuser('Wien', 'Kino', 10, 15 )
sights_wien = Haeuser('Wien', 'Sehenswürdigkeiten', 10, 15 )
kiosk_wien = Haeuser('Wien', 'Kiosk für Getränke', 1, 5 )
tankstelle_wien = Haeuser('Wien', 'Tankstelle', 97, wien.entfernung * 0.10 )
### BERN
hotel_bern = Haeuser('Bern', 'Hotel', 100, 60 )
ferienwohnung_bern = Haeuser('Bern', 'Ferienwohnung', 97, 40 )
restaurant_bern = Haeuser('Bern', 'Restaurant', 1, 30 )
imbiss_bern = Haeuser('Bern', 'Imbiss', 1, 20 )
kino_bern = Haeuser('Bern', 'Kino', 10, 15 )
sights_bern = Haeuser('Bern', 'Sehenswürdigkeiten', 10, 15 )
kiosk_bern = Haeuser('Bern', 'Kiosk für Getränke', 1, 5 )
tankstelle_bern = Haeuser('Bern', 'Tankstelle', 97, bern.entfernung * 0.10 )
### WARSCHAU
hotel_warschau = Haeuser('Warschau', 'Hotel', 100, 60 )
ferienwohnung_warschau = Haeuser('Warschau', 'Ferienwohnung', 97, 40 )
restaurant_warschau = Haeuser('Warschau', 'Restaurant', 1, 30 )
imbiss_warschau = Haeuser('Warschau', 'Imbiss', 1, 20 )
kino_warschau = Haeuser('Warschau', 'Kino', 10, 15 )
sights_warschau = Haeuser('Warschau', 'Sehenswürdigkeiten', 10, 15 )
kiosk_warschau = Haeuser('Warschau', 'Kiosk für Getränke', 1, 5 )
tankstelle_warschau = Haeuser('Warschau', 'Tankstelle', 97, warschau.entfernung * 0.10 )
### AMSTERDAM
hotel_amsterdam = Haeuser('Amsterdam', 'Hotel', 100, 60 )
ferienwohnung_amsterdam = Haeuser('Amsterdam', 'Ferienwohnung', 97, 40 )
restaurant_amsterdam = Haeuser('Amsterdam', 'Restaurant', 1, 30 )
imbiss_amsterdam = Haeuser('Amsterdam', 'Imbiss', 1, 20 )
kino_amsterdam = Haeuser('Amsterdam', 'Kino', 10, 15 )
sights_amsterdam = Haeuser('Amsterdam', 'Sehenswürdigkeiten', 10, 15 )
kiosk_amsterdam = Haeuser('Amsterdam', 'Kiosk für Getränke', 1, 5 )
tankstelle_amsterdam = Haeuser('Amsterdam', 'Tankstelle', 97, amsterdam.entfernung * 0.10 )
### Standard Häuser in Array
travel_ziele = ['( 1 ) Hotel', '( 2 ) Ferienwohnung', '( 3 ) Restaurant', '( 4 ) Imbiss', '( 5 ) Kino', '( 6 ) Sehenswürdigkeit', '( 7 ) Kiosk', '( 8 ) Tankstelle']
### BERLIN
werkstatt = Haeuser('Berlin', 'Werkstatt', 1, 100 - (car1.damage * 5))
restaurant = Haeuser('Berlin', 'Restaurant', 2, 25)
imbiss = Haeuser('Berlin', 'Imbiss', 1, 15 )
kiosk = Haeuser('Berlin', 'Kiosk', 1, 5)


#%% SPIEL - START

print('Herzlich Willkommen zum Panda Travel - Adventure')
print()
print('Ein heiteres kleines Rollenspiel')
print('Ziel des Spiels ist es, deinem Beruf nachzugehen und alle Hauptstädte zu besuchen')
print()

#%% Aufbau Spieler

trenner()
print('Als erstes erstellst du deinen Charakter:')
print()
name = input('Bitte tippe den Namen ein: ')
sex = input('männlich (m) oder weiblich (w) ?: ')
while sex.lower() != 'm' and sex.lower() != 'w':
    print('###')
    print('Bite nur m oder w als Eingabe verwenden:')
    print('###')
    sex = input('männlich (m) oder weiblich (w) ?: ')
age = '0'
age_check = [i for i in range(1, 100)]
while True:
    try:
        age = input('Bitte nenne mir das Alter: ')
        if int(age) in age_check:
            break
        elif int(age) <= 0 or int(age) >= 100:
            print('###')
            print('Bitte nur Zahlen von 1 - 99 eingeben')
            print('###')
    except :
        print('###')
        print('Bitte nur Zahlen von 1 - 99 eingeben')
        print('###')
print()
player1 = Menschen(name.capitalize(), sex.lower(), int(age), 0)
print('\n')

#%% Aufbau Fahzeug
trenner()
if player1.age >= 18:
    print(f'Als nächstes erstellen wir dein Auto, da Du schon älter als 18 bist:')
    print()
    marke = input('Nenne die Automarke: ')
    modell = input('Nenne das Modell: ')
    farbe = input('Nenne mit die Farbe: ')
    print()
    car1 = Autos(marke.capitalize(), modell.capitalize(), farbe)
    print()
    print('200€ für die Kaufgebühr wurden deinem Guthaben abgezogen')
    player1.weniger_geld(200)
    print('\n')
else:
    print(f'Da Du noch keine 18 Jahre alt bist, müssen wir zuerst einen Führerschein machen.')
    print('Starten wir also mit der Fahschule. Wenn du 8 von 10 Fragen richtig beantwortet hast, bekommst Du deinen Füherschein.')
    print('Falls nicht, musst Du die Prüfung wiederholen')
    print('Die Gebühren für den Führerschein inklusive Fahrprüfung sind 200€.')
    print()
    fahrprüfung()
    print('Herzlichen Glückwunsch zur bestandenen Fahrprüfung, die 200€ wurden deinem Kontostand abgezogen')
    print('\n')
    print(f'Als nächstes erstellen wir dein Auto, da Du jetzt deinen Führerschein hast und wir schenken dir zum bestehen der Fahrerlaubnis die Kaufgebühr:')
    print()
    marke = input('Nenne die Automarke: ')
    modell = input('Nenne das Modell: ')
    farbe = input('Nenne mit die Farbe: ')
    print()
    car1 = Autos(marke.capitalize(), modell.capitalize(), farbe)
    print('\n')

#%% Aufbau zu Hause

trenner()
print(f'Als letztes bauen wir dein zu Hause:')
print()
haus = 'zu Hause'
while True:
    try:
        anzahl_zimmer = int(input('Wieviele Zimmer soll dein zu Hause haben ?: '))
    except :
        print('###')
        print('Bitte nur Zahlen eingeben')
        print('###')
    else: 
        break

print()
berlin = Staedte('Berlin', 3645000, 0)
zuhause = Haeuser('Berlin', 'zu Hause', anzahl_zimmer, 10)
print(f'Dein neues Haus wurde mit {anzahl_zimmer} Zimmern in {berlin.ortsname} gebaut und Du bist eingezogen.')
print('\n')
input('- Weiter mit beliebiger Taste -')

#%% Hauptmenü

game = 'play'
universitaet_stufe = 0
travels = 0
while game != 'exit':
    trenner()
    print()
    print('H A U P T M E N Ü')
    print()
    print('( 1 ) Spielerstatus')
    print('( 2 ) Fahrzeugstatus')
    print('( 3 ) Arbeiten gehen')
    print('( 4 ) Auf Reise gehen')
    print('( 5 ) Spielerstatus erhöhen')
    print('( 6 ) Spiel beenden')
    print()
    hauptmenue_check = [i for i in range(1, 7)]
    while True:
        try:
            eingabe_hauptmenue = (input('Eingabe: '))
            if int(eingabe_hauptmenue) in hauptmenue_check:
                    eingabe_hauptmenue = int(eingabe_hauptmenue)
                    break
            elif int(eingabe_hauptmenue) <= 0 or int(eingabe_hauptmenue) >= 7:
                print()
                print('###')
                print('Bitte nur Zahlen von 1 - 6 eingeben')
                print('###')
                print()
        except :
            print()
            print('###')
            print('Bitte nur Zahlen von 1 - 6 eingeben')
            print('###')
            print()

#%% ( 1 ) ABFRAGE SPIELERSTATUS

    if eingabe_hauptmenue == 1:
        print()
        print(f'{player1.name}, {player1.age} Jahre alt verfügt aktuell über:')
        print(f'{player1.health}% Gesundheit')
        print(f'{player1.hungry}% gesättigten Hunger')
        print(f'{player1.thursty}% gestillten Durst')
        print(f'{player1.money}€ Guthaben') 
        print()
        input('- Weiter mit beliebiger Taste -')

#%% ( 2 ) ABFRAGE FAHRZEUGSTATUS

    elif eingabe_hauptmenue == 2:
        print()
        print(f'Der {car1.marke} {car1.modell} in {car1.farbe} verfügt aktuell über:')
        print(f'{car1.fuel}% Tankfüllung')
        print(f'{car1.damage}% Zustand')
        print()
        input('- Weiter mit beliebiger Taste -')

#%% ( 3 ) START BERUF

    elif eingabe_hauptmenue == 3:
        trenner()
        print()
        print('B E R U F')

#%%         - WAHL ERSTER BERUF

        if beruf.beruf == 'Testing':
            eingabe_beruf1 = 0           
            print()
            print('Da Du bisher noch keinen Beruf gewählt hast musst Du diesen als erstes wählen:')
            print('Du hast die Möglichkeit sofort in einen einfachen Beruf zu starten, später kannst Du den Beruf nochmal wechseln oder zur Universität gehen um einen besseren Beruf zu bekommen.\n')            
            while eingabe_beruf1 >= 4 or eingabe_beruf1 == 0:
                eingabe_beruf1 = int(input('( 1 )  Verkäufer im Geschäft ( 8Stunden pro Tag, 50€ Vedienst pro Tag )\n( 2 )  Büroangestellter ( 8Stunden pro Tag, 50€ Vedienst pro Tag )\n( 3 )  Handwerker ( 8Stunden pro Tag, 50€ Vedienst pro Tag )\n\nEingabe: '))
                if eingabe_beruf1 == 1:
                    if player1.sex == 'm':
                        beruf = Berufe('Verkäufer', 8, 75)
                        print()
                        input('- Weiter mit beliebiger Taste -')
                    else:
                        beruf = Berufe('Verkäuferin', 8, 75)
                        print()
                        input('- Weiter mit beliebiger Taste -')
                elif eingabe_beruf1 == 2:
                    if player1.sex == 'm':
                        beruf = Berufe('Büroangestellter', 8, 75)
                        print()
                        input('- Weiter mit beliebiger Taste -')
                    else:
                        beruf = Berufe('Büroangestellte', 8, 75)
                        print()
                        input('- Weiter mit beliebiger Taste -')
                elif eingabe_beruf1 == 3:
                    if player1.sex == 'm':
                        beruf = Berufe('Handwerker', 8, 75)
                        print()
                        input('- Weiter mit beliebiger Taste -')
                    else:
                        beruf = Berufe('Handwerkerin', 8, 75)
                        print()
                        input('- Weiter mit beliebiger Taste -')
                else:
                    print('!!! Bitte nutze nur die verfügbaren Nummern !!!')         
        else:

#%%         - MENÜ BERUF
            
            eingabe_beruf2 = 0
            while eingabe_beruf2 != 4:
                print()
                print(f'Dein aktueller Beruf ist {beruf.beruf} in dem du {beruf.gehalt}€ pro Tag verdienst und {beruf.stunden} Stunden arbeitest\n')
                print(f'Wenn Du arbeiten möchtest wird zufällig 1 von 3 unerschielichen Minispielen zu erledigen sein oder mit ein bisschen Glück ist der Chef nicht im Haus :-)\n')
                eingabe_beruf2 = int(input(f'Was möchtest Du machen:\n( 1 ) {beruf.stunden} Stunden arbeiten um {beruf.gehalt}€ zu verdienen\n( 2 ) Zur Universität gehen um neue Berufe zu erlernen\n( 3 ) Beruf wechseln\n( 4 ) Zurück zum Hauptmenü\n\nEingabe: '))
                
#%%         - ARBEITEN
                
                if eingabe_beruf2 == 1:
                    if  player1.health - beruf.stunden * 5 < 0 :
                        print('###')
                        print(f'Leider genügt dein Spielerstatus nicht aus um zu arbeiten. Du solltest deine Gesundheit vorher steigern')
                        print('###') 
                        input('\n- Weiter mit beliebiger Taste -')
                    elif player1.hungry - beruf.stunden * 5 < 0:
                        print('###')
                        print(f'Leider genügt dein Spielerstatus nicht aus um zu arbeiten. Du solltest deinen Hunger vorher steigern')
                        print('###') 
                        input('\n- Weiter mit beliebiger Taste -')  
                    elif player1.thursty - beruf.stunden * 5 < 0:
                        print('###')
                        print(f'Leider genügt dein Spielerstatus nicht aus um zu arbeiten. Du solltest deinen Durst vorher steigern')
                        print('###') 
                        input('\n- Weiter mit beliebiger Taste -')
                    else:
                        trenner()
                        print('Willkommen auf der Arbeit')
                        print()
                        spielauswahl()
                        if travels > 0:
                            beruf.arbeiten_mit_travels()
                            travels -= 1
                        elif travels == 0:
                            beruf.arbeiten_ohne_travels()
                        print()
                        input('- Weiter mit beliebiger Taste -')

#%%         - UNIVERSITÄT

                elif eingabe_beruf2 == 2:
                    if player1.uni_stufe == 0:
                        universitaet_abfrage1 = ''
                        while universitaet_abfrage1 != 'exit':
                            trenner()
                            print()
                            print('U N I V E R S I T Ä T')
                            print()
                            print('Herzlichen Wilkommen in der Universität')
                            print()
                            print('Hier hast Du die Möglichkeit die Universität zu besuchen.')
                            print()
                            print('Es gibt zwei Stufen:')
                            print('Stufe 1 schaltet in - Beruf wechseln - 3 neue, fortgeschrittene und besser bezahlte Berufe frei.')
                            print('Stufe 2 schaltet in - Beruf wechseln - 3 neue Traumberufe frei mit dem bestmöglichen Gehalt.')
                            print()
                            print('Bevor Du Stufe 2 freischaltest, musst Du Stufe 1 freigeschaltet haben.')
                            print()
                            print('( 1 ) Stufe 1 freischalten für 2.000€.')
                            print('( 2 ) Stufe 2 freischalten für 5.000€.')
                            print('( 3 ) Zurück zum Hauptmenü')
                            print()
                            universitaet_abfrage1 = int(input('Eingabe: '))
                            if universitaet_abfrage1 == 1:
                                if player1.money - 2000 < 0:
                                    print('Leider genügt dein Guthaben nicht aus um die 2.000€ für die Universitäts-Stufe zu zahlen.')
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                    trenner()
                                    universitaet_abfrage1 = 'exit'
                                else:
                                    player1.weniger_geld(2000)
                                    print()
                                    player1.mehr_uni(1)
                                    print()
                                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                                    trenner()
                                    universitaet_abfrage1 = 'exit'
                            elif universitaet_abfrage1 == 2:
                                    print('Du musst als erstes Stufe 1 freischalten.')
                                    print()
                                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                                    trenner()
                            elif universitaet_abfrage1 == 3 or universitaet_abfrage1 > 3:
                                    universitaet_abfrage1 = 'exit'
                                    trenner()
                    elif player1.uni_stufe == 1:
                        universitaet_abfrage1 = ''
                        while universitaet_abfrage1 != 'exit':
                            trenner()
                            print()
                            print('U N I V E R S I T Ä T')
                            print()
                            print('Herzlichen Wilkommen in der Universität')
                            print()
                            print('Hier hast Du die Möglichkeit die Universität zu besuchen.')
                            print()
                            print('Es gibt zwei Stufen:')
                            print('Stufe 1 hast Du bereits freigeschaltet')
                            print('Stufe 2 schaltet in - Beruf wechseln - 3 neue Traumberufe frei mit dem best möglichen Gehalt.')
                            print()
                            print('Bevor Du Stufe 2 freigeschaltest, musst Du Stufe 1 freigeschaltet haben.')
                            print()
                            print('( 1 ) Stufe 2 freischalten für 5.000€.')
                            print('( 2 ) Zurück zum Hauptmenü')
                            print()
                            universitaet_abfrage1 = int(input('Eingabe: '))
                            if universitaet_abfrage1 == 1:
                                if player1.money - 5000 < 0:
                                    print('Leider genügt dein Guthaben nicht aus um die 5.000€ für die Universitäts-Stufe zu zahlen.')
                                    print()
                                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                                    trenner()
                                    universitaet_abfrage1 = 'exit'
                                else:
                                    player1.weniger_geld(5000)
                                    player1.mehr_uni(1)
                                    print()
                                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                                    trenner()
                                    universitaet_abfrage1 = 'exit'
                            elif universitaet_abfrage1 == 2 or universitaet_abfrage1 > 2:                                    
                                    universitaet_abfrage1 = 'exit'
                                    trenner()
                    elif player1.uni_stufe == 2:
                        universitaet_abfrage1 = ''
                        while universitaet_abfrage1 != 'exit':
                            trenner()
                            print()
                            print('U N I V E R S I T Ä T')
                            print()
                            print('Herzlichen Wilkommen in der Universität')
                            print()
                            print('Hier hast Du die Möglichkeit die Universität zu besuchen.')
                            print()
                            print('Es gibt zwei Stufen:')
                            print('Stufe 1 hast Du bereits freigeschaltet')
                            print('Stufe 2 hast Du bereits freigeschaltet')
                            print()
                            print('Hier gibt es nichts mehr zu tun für Dich')
                            print()
                            input('- zurück zum Hauptmenü mit beliegbiger Taste -')    
                            trenner()                                                          
                            universitaet_abfrage1 = 'exit'         
                            trenner()      

#%%         - BERUF WECHSELN
                
                elif eingabe_beruf2 == 3:
                    trenner()
                    print()
                    eingabe_berufwechsel1 = 0
                    if player1.uni_stufe == 0:                        
                        while eingabe_berufwechsel1 >= 4 or eingabe_berufwechsel1 == 0:
                            beruf.beruf_anzeigen()
                            print()
                            print('Standard Berufe stehen zur Auswahl:')
                            print()
                            print('( 1 )  Verkäufer im Geschäft ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print('( 2 )  Büroangestellter ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print('( 3 )  Handwerker ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print()
                            print('Um deinen Beruf zu behalten wähle deinen aktuellen Beruf aus.')
                            print()
                            eingabe_berufwechsel1 = int(input('Eingabe: '))
                            if eingabe_berufwechsel1 == 1:
                                if player1.sex == 'm':
                                    beruf = Berufe('Verkäufer', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Verkäuferin', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 2:
                                if player1.sex == 'm:':
                                    beruf = Berufe('Büroangestellter', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Büroangestellte', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 3:
                                if player1.sex == 'm':
                                    beruf = Berufe('Handwerker', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Handwerkerin', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            else:
                                print('!!! Bitte nutze nur die verfügbaren Nummern !!!')
                            trenner()

                    elif player1.uni_stufe == 1:
                        while eingabe_berufwechsel1 >= 7 or eingabe_berufwechsel1 == 0:
                            beruf.beruf_anzeigen()
                            print()
                            print('Standard Berufe stehen zur Auswahl:')
                            print()
                            print('( 1 )  Verkäufer im Geschäft ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print('( 2 )  Büroangestellter ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print('( 3 )  Handwerker ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print()
                            print('Super Berufe stehen zu Auswahl:')
                            print()
                            print('( 4 )  Arzt ( 8Stunden pro Tag, 150€ Vedienst pro Tag )')
                            print('( 5 )  Pilot ( 8Stunden pro Tag, 150€ Vedienst pro Tag )')
                            print('( 6 )  TV Moderator ( 8Stunden pro Tag, 150€ Vedienst pro Tag )')
                            print()
                            print('Um deinen Beruf zu behalten wähle deinen aktuellen Beruf aus.')
                            print()
                            eingabe_berufwechsel1 = int(input('Eingabe: '))
                            if eingabe_berufwechsel1 == 1:
                                if player1.sex == 'm':
                                    beruf = Berufe('Verkäufer', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Verkäuferin', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 2:
                                if player1.sex == 'm:':
                                    beruf = Berufe('Büroangestellter', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Büroangestellte', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 3:
                                if player1.sex == 'm':
                                    beruf = Berufe('Handwerker', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Handwerkerin', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 4:
                                if player1.sex == 'm':
                                    beruf = Berufe('Arzt', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Ärztin', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 5:
                                if player1.sex == 'm':
                                    beruf = Berufe('Pilot', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Pilotin', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 6:
                                if player1.sex == 'm':
                                    beruf = Berufe('TV Moderator', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')  
                                else:
                                    beruf = Berufe('TV Moderatorin', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')                              
                            else:
                                print('!!! Bitte nutze nur die verfügbaren Nummern !!!')
                            trenner()
                        
                    elif player1.uni_stufe == 2:
                        while eingabe_berufwechsel1 >= 10 or eingabe_berufwechsel1 == 0:
                            beruf.beruf_anzeigen()
                            print()
                            print('Standard Berufe stehen zur Auswahl:')
                            print()
                            print('( 1 )  Verkäufer im Geschäft ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print('( 2 )  Büroangestellter ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print('( 3 )  Handwerker ( 8Stunden pro Tag, 75€ Vedienst pro Tag )')
                            print()
                            print('Super Berufe stehen zu Auswahl:')
                            print()
                            print('( 4 )  Arzt ( 8Stunden pro Tag, 150€ Vedienst pro Tag )')
                            print('( 5 )  Pilot ( 8Stunden pro Tag, 150€ Vedienst pro Tag )')
                            print('( 6 )  TV Moderator ( 8Stunden pro Tag, 150€ Vedienst pro Tag )')
                            print()
                            print('( 7 )  Hollywood Film-Star ( 6Stunden pro Tag, 250€ Vedienst pro Tag )')
                            print('( 8 )  Sänger ( 6Stunden pro Tag, 250€ Vedienst pro Tag )')
                            print('( 9 )  Präsident ( 6Stunden pro Tag, 250€ Vedienst pro Tag )')
                            print()
                            print('Um deinen Beruf zu behalten wähle deinen aktuellen Beruf aus.')
                            print()
                            eingabe_berufwechsel1 = int(input('Eingabe: '))
                            if eingabe_berufwechsel1 == 1:
                                if player1.sex == 'm':
                                    beruf = Berufe('Verkäufer', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Verkäuferin', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 2:
                                if player1.sex == 'm:':
                                    beruf = Berufe('Büroangestellter', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Büroangestellte', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 3:
                                if player1.sex == 'm':
                                    beruf = Berufe('Handwerker', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Handwerkerin', 8, 75)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 4:
                                if player1.sex == 'm':
                                    beruf = Berufe('Arzt', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Ärztin', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 5:
                                if player1.sex == 'm':
                                    beruf = Berufe('Pilot', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                                else:
                                    beruf = Berufe('Pilotin', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 6:
                                if player1.sex == 'm':
                                    beruf = Berufe('TV Moderator', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')  
                                else:
                                    beruf = Berufe('TV Moderatorin', 8, 150)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')  
                            elif eingabe_berufwechsel1 == 7:
                                if player1.sex == 'm':
                                    beruf = Berufe('Hollywood Film-Star', 6, 250)
                                    print()
                                    input('- Weiter mit beliebiger Taste -') 
                                else:
                                    beruf = Berufe('Hollywood Film-Star', 6, 250)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')
                            elif eingabe_berufwechsel1 == 8:
                                if player1.sex == 'm':
                                    beruf = Berufe('Sänger', 6, 250)
                                    print()
                                    input('- Weiter mit beliebiger Taste -') 
                                else:
                                    beruf = Berufe('Sängerin', 6, 250)
                                    print()
                                    input('- Weiter mit beliebiger Taste -') 
                            elif eingabe_berufwechsel1 == 9:
                                if player1.sex == 'm':
                                    beruf = Berufe('Präsident', 6, 250)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')   
                                else:
                                    beruf = Berufe('Präsidentin', 6, 250)
                                    print()
                                    input('- Weiter mit beliebiger Taste -')                      
                            else:
                                print('!!! Bitte nutze nur die verfügbaren Nummern !!!')
                            trenner()
                
#%% ( 4 ) START REISEN

    elif eingabe_hauptmenue == 4:
        exit = ''
        while exit != 'exit':
            eingabe_reisen = 0
            trenner()
            print()
            print('R E I S E N')
            print()
            print('Willkommen im Reisemenü. Hier hast Du die Auswahl verschiedenster Ausflugsziele.')
            print('Ziel einer Reise ist es, eine Auszeit vom Alltag zu bekommen. Wärend jeder Reise hast du zusätzlich die Möglichkeit einen kleinen Schatz zu finden der zufällig erscheint.')
            print('Darüber hinaus bist Du durch den Urlaub so sehr erholt, dass Du für die nächsten 3 Arbeitstage keinen Spielerstatus verlierst.')
            print()
            for stadt in staedte:
                print(stadt)
            print('( 8 ) Zurück zum Hauptmenü')
            print()
            eingabe_reisen = int(input('Eingabe: '))

#%%         - Reise nach London

            if eingabe_reisen == 1:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_london.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in London')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_london.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Londoner Hotel mit Blick auf die Themse')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_london.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_london.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf den St.James Park, wo auch der Buckingham Palace zu sehen ist.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_london.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_london.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf das London-Eye.')
                                print('Es gab heute klassisch Beef Wellington und Yorkshire Pudding.')
                                print(f'Die Kosten in Höhe von {restaurant_london.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_london.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der Oxford Street hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in London, Fish & Chips gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_london.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_london.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " The Prince Charles Cinema " und hast dir den neuesten Film " 00 Panda - Lizenz zum Kitzeln " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_london.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_london.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast eine Themsenfahrt unternommen, gestartet von Westminster bis zur Tower Bridge')
                                print(f'Die Kosten in Höhe von {sights_london.kosten}€ für die Fahrt auf der Themse wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('auf dem Schiff der Themsenfahrt')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_london.kosten)
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem klassischen Londoner Pub und hast dir eine kühles Glas frisch gezapftest Stout Lager gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_london.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_london.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle undhast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {london.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_london.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

#%%         - Reise nach Paris

            elif eingabe_reisen == 2:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_paris.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in Paris')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_paris.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Pariser Hotel mit Blick auf den Eifelturm')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_paris.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_paris.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf den Arc de Triumph.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_paris.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_paris.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf den Louvre.')
                                print('Es gab heute klassisch Ratatouille und Mousse au chocolat.')
                                print(f'Die Kosten in Höhe von {restaurant_paris.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_paris.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der Champs-Elysées hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in Paris, einen leckeren Crêpes gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_paris.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_paris.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " Le Balzac Cinéma " und hast dir den neuesten Film " Pandá - der Profi " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_paris.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_paris.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast an einen Rundgang durch Schloss Versailles teilgenommen und mächtig viel Fotos von der atemberaubendem Anlage gemacht.')
                                print(f'Die Kosten in Höhe von {sights_paris.kosten}€ für die Fahrt auf der Themse wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('im Schloss Versailles')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_paris.kosten)
                                player1.thursty = 100
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem kleinen Café und hast dir ein kühles spritziges Glas Champagner gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_paris.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_paris.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle und hast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {paris.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_paris.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

#%%         - Reise nach Barcelona

            elif eingabe_reisen == 3:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_barcelona.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in Barcelona')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_barcelona.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Barcelona Hotel mit Blick auf die Sagrada Familia')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_barcelona.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_barcelona.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf das gotische Viertel.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_barcelona.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_barcelona.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf das Picasso Museum.')
                                print('Es gab heute klassisch Paella und Tortillas.')
                                print(f'Die Kosten in Höhe von {restaurant_barcelona.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_barcelona.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der La rambla hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in Barcelona, einen leckere Portion Churros gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_barcelona.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_barcelona.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " Cinemes Verdi " und hast dir den neuesten Film " Pandas Labyrinth " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_barcelona.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_barcelona.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast an einen Rundgang durch Camp Nou teilgenommen, dem Stadion von FC Barcelona und eine Sammelkarte des Vereins mit allen Unterschriften mitgenommen.')
                                print(f'Die Kosten in Höhe von {sights_barcelona.kosten}€ für den Rundgang wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('im Camp Nou')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_barcelona.kosten)
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem kleinen Café und hast dir einen leckeren, frisch zubereiteten Sangria gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_barcelona.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_barcelona.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle und hast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {barcelona.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_barcelona.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

#%%         - Reise nach Wien

            elif eingabe_reisen == 4:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_wien.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in Wien')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_wien.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Barcelona Hotel mit Blick auf die Domkirche St. Stephan')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_wien.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_wien.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf die Wiener Staatsoper.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_wien.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_wien.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf die Hofburg.')
                                print('Es gab heute klassisch Wiener Schnitzel mit Pommes.')
                                print(f'Die Kosten in Höhe von {restaurant_wien.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_wien.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der Mariahilfer Straße hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in Wien, einen leckeres Stück Sachertorte gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_wien.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_wien.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " Burgkino " und hast dir den neuesten Film " Panda - Der junge Kaiser " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_wien.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_wien.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast an einen Rundgang durch Schloss Schönbrunn teilgenommen, und viele Fotos dieses tollen und imposanten Schlosses gemacht.')
                                print(f'Die Kosten in Höhe von {sights_wien.kosten}€ für den Rundgang wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('auf dem Vorplatz des Schlosses')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_wien.kosten)
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem kleinen Café und hast dir einen leckeren Wiener Melange gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_wien.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_wien.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle und hast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {wien.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_wien.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

#%%         - Reise nach Bern

            elif eingabe_reisen == 5:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_bern.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in Bern')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_wien.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Berner Hotel mit Blick auf die Zytglogge')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_bern.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_bern.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf den Käfigturm.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_bern.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_bern.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf die Berner Altstadt.')
                                print('Es gab heute klassisch Bärner Platte.')
                                print(f'Die Kosten in Höhe von {restaurant_bern.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_bern.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der Spitalgasse hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in Bern, einen leckeres Stück Butterzopf gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_bern.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_bern.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " Kino REX " und hast dir den neuesten Film " Das Wunder von Panda " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_bern.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_bern.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast an einen Rundgang durch den Botanischer Garten der Universität Bern teilgenommen, und viele Fotos dieses tollen und imposanten Schlosses gemacht.')
                                print(f'Die Kosten in Höhe von {sights_bern.kosten}€ für den Rundgang wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('im Botanischer Garten')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_bern.kosten)
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem kleinen Café und hast dir einen leckeres Glas Rivella gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_bern.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_bern.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle und hast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {bern.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_bern.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

#%%         - Reise nach Warschau

            elif eingabe_reisen == 6:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_warschau.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in Warschau')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_warschau.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Warschauer Hotel mit Blick auf den Lazienki Park')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_warschau.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_warschau.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf den Wilanow Palast.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_warschau.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_warschau.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf die Warschauer Altstadt.')
                                print('Es gab heute klassisch Masurischen Fisch mit Pilzen.')
                                print(f'Die Kosten in Höhe von {restaurant_warschau.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_warschau.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der Rondo Radoslawa hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in Warschau, eine Portion Zygmuntówka gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_warschau.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_warschau.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " Kinoteka " und hast dir den neuesten Film " Der gelobte Panda " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_warschau.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_warschau.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast an einen Rundgang durch das Museum des Warschauer Aufstandes teilgenommen.')
                                print(f'Die Kosten in Höhe von {sights_warschau.kosten}€ für den Rundgang wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('im Museum des Warschauer Aufstandes')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_warschau.kosten)
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem kleinen Café und hast dir einen leckeres Glas Zubrovka gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_warschau.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_warschau.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle und hast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {warschau.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_warschau.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

#%%         - Reise nach Amsterdam

            elif eingabe_reisen == 7:
                if player1.money - tankstelle_london.kosten + 100 < 0:
                    print(f'Dein Budget reicht nicht aus um in den Urlaub zu fahren. Du benötigst mindestens {tankstelle_amsterdam.kosten + 100}€')
                else:
                    eingabe_in_reise1 = 0
                    car1.anreise_urlaub()
                    player1.anreise_urlaub()
                    eingabe_reisen_exit = ''
                    while eingabe_reisen_exit != 'exit':
                        trenner()
                        print()
                        print('Willkommen in Amsterdam')
                        print()
                        player1.im_urlaub()
                        print()
                        car1.im_urlaub()
                        print()
                        for ziel in travel_ziele:
                            print(ziel)
                        print('( 9 ) Zurück nach Hause')
                        print()
                        eingabe_in_reise1 = int(input('Eingabe: '))
                        if eingabe_in_reise1 != 8 and car1.fuel == 0:
                            print()
                            trenner()
                            print()
                            print('Dein Tank von deinem Auto ist von der Anreise leer. Du solltest als erstes zur Tankstelle bevor Du weiter machst!')
                            print()
                        else:
                            if eingabe_in_reise1 == 1:
                                player1.weniger_geld(hotel_amsterdam.kosten)
                                player1.health = 100
                                player1.hungry = 100
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen im Amsterdamer Hotel mit Blick auf den Vondelark')
                                print('Du hast vom reichhaltigen Frühstückbuffet profitiert und dein Hunger und Durst sind komplett gestillt')
                                print(f'Die Kosten in Höhe von {hotel_amsterdam.kosten}€ für das Hotel wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 2:
                                player1.weniger_geld(ferienwohnung_amsterdam.kosten)
                                player1.health = 100
                                player1.weniger_hungry(30)
                                player1.weniger_thursty(30)
                                print()
                                trenner()
                                print()
                                print('Du hast wunderbar geschlafen in der Ferienwohnung mit Blick auf die Grachten.')
                                print(f'Die Kosten in Höhe von {ferienwohnung_amsterdam.kosten}€ für die Ferienwohnung wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 3:
                                player1.weniger_geld(restaurant_amsterdam.kosten)
                                player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Du hast tolles kleines Restaurant gefunden mit Blick auf ddas Van Gogh Museum.')
                                print('Es gab heute klassisch holländischen Matjes mit dicken Pommes.')
                                print(f'Die Kosten in Höhe von {restaurant_amsterdam.kosten}€ für das Restaurant wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 4:
                                player1.weniger_geld(imbiss_amsterdam.kosten)
                                if player1.hungry <= 50:
                                    player1.mehr_hungry(50)
                                else:
                                    player1.hungry = 100
                                print()
                                trenner()
                                print()
                                print('Ein kleiner Imbiss auf der Kalverstraat hat dich überzeugt.')
                                print('Du hast dir, wie kann es ander sein in Amsterdam, eine Portion Frikandell spezial gegönnt')
                                print(f'Die Kosten in Höhe von {imbiss_amsterdam.kosten}€ für den Imbiss wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 5:
                                player1.weniger_geld(kino_amsterdam.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du warst im bekannten " Pathé Arena " und hast dir den neuesten Film " New Panda Turbo " angeschaut.')
                                print(f'Die Kosten in Höhe von {kino_amsterdam.kosten}€ für das Kino wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 6:
                                player1.weniger_geld(sights_amsterdam.kosten)
                                player1.weniger_hungry(20)
                                player1.weniger_thursty(20)
                                print()
                                trenner()
                                print()
                                print('Du hast an einen Rundgang durch das Anne-Frank-Haus teilgenommen.')
                                print(f'Die Kosten in Höhe von {sights_amsterdam.kosten}€ für den Rundgang wurden von deinem Konto abgezogen')
                                print()
                                random_bonus('im Anne-Frank-Haus')
                                print()
                            elif eingabe_in_reise1 == 7:
                                player1.weniger_geld(kiosk_amsterdam.kosten)
                                player1.thursty = 100
                                print()
                                trenner()
                                print()
                                print('Du warst in einem kleinen Café und hast dir einen leckeres Glas Chocomel gegönnt')
                                print(f'Die Kosten in Höhe von {kiosk_amsterdam.kosten}€ für den Pub wurden von deinem Konto abgezogen')
                                print()
                            elif eingabe_in_reise1 == 8:
                                player1.weniger_geld(tankstelle_amsterdam.kosten)
                                player1.weniger_thursty(20)
                                player1.weniger_hungry(20)
                                car1.fuel = 100
                                print()
                                trenner()
                                print()
                                print('Du warst an der Tankstelle und hast dein Auto getankt.')
                                print(f'Die Tank-Kosten bei einer Entfernung von {amsterdam.entfernung}km von Berling entfernt')
                                print(f'waren {tankstelle_amsterdam.kosten}€ und wurden von deinem Konto abgezogen')
                                print()                            
                            if eingabe_in_reise1 == 9:
                                print()
                                trenner()
                                print()
                                print('Du bist wieder zu Hause')
                                print(f'Du hattest einen wunderschönen Urlaub und hast tolle Erinnerungen gesammelt.')
                                print()
                                travels += 3
                                eingabe_reisen_exit = 'exit'

            elif eingabe_reisen == 8:
                print('- Weiter mit beliebiger Taste -')
                exit = 'exit'
#%% ( 5 ) SPIELESTATUS ERHÖHEN
    
    
    elif eingabe_hauptmenue == 5:
        eingabe_status = ''
        while eingabe_status != 'exit':
            trenner()
            print()
            print('S T A T U S  -  E R H Ö H U N G E N')
            print()
            print(f'Hier kannst Du dich und dein Fahrzeug wieder auf 100% bringen')
            print()
            print(f'{player1.name}, {player1.age} Jahre alt verfügt aktuell über:')
            print(f'{player1.health}% Gesundheit')
            print(f'{player1.hungry}% gesättigten Hunger')
            print(f'{player1.thursty}% gestillten Durst')
            print(f'{player1.money}€ Guthaben')
            print()
            print('( 1 ) Werkstatt:')
            print(f'          - Die Reparatur deines Fahrzeugs kostet 5€ pro Prozentpunkt:')
            print(f'          - Fahzeugstatus: {car1.damage} %')
            print(f'          - Reparaturkosten: {(100 - car1.damage) * 5}€')
            print()
            print('( 2 ) Restaurant:')
            print('          - Die Mahlzeit in einem Restaurant kostet 25€ und bringt dich auf 100% Hunger:')
            print(f'          - Gesundheitsstatus: {player1.hungry} %')
            print()
            print(f'( 3 ) Imbiss:')
            print(f'          - Die Mahlzeit in einem Imbiss kostet 15€ und bringt dir 50% mehr gesättigten Hunger:')
            print(f'          - Gesundheitsstatus: {player1.hungry} %')
            print()
            print(f'( 4 ) Kiosk:')
            print(f'          - Das Getränk in einem Kiosk kostet 5€ und bringt dich auf 100% Durst:')
            print(f'          - Gesundheitsstatus: {player1.thursty} %')
            print()
            print(f'( 5 ) Schlafen:')
            print(f'          - Das Schlafen in deinem Haus kostet 10€ und bringt dich auf 100% Gesundheit:')
            print(f'          - Gesundheitsstatus: {player1.health} %')
            print()
            print('( 6 ) Zurück zum Hauptmenü')
            eingabe_status1 = int(input('Eingabe: '))
            print()
            if eingabe_status1 == 1:
                if player1.money - ((100 - car1.damage) * 5) < 0:
                    print(f'Leider genügt dein Guthaben nicht aus um die {(100 - car1.damage) * 5}€ für die Werkstatt zu zahlen.')
                    print()
                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                    trenner()
                else:
                    player1.weniger_geld((100 - car1.damage) * 5)
                    car1.damage = 100
                    print(f'Die Reparatur wurde durchgeführt, die Kosten in Höhe von {(100 - car1.damage) * 5}€ wurden deinem Konto abgezogen')
                    print()
                    input('- weiter mit beliebiger Taste')
            elif eingabe_status1 == 2:
                if player1.money - (restaurant.kosten) < 0:
                    print(f'Leider genügt dein Guthaben nicht aus um die {restaurant.kosten}€ für das Restaurant zu zahlen.')
                    print()
                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                    trenner()
                else:
                    player1.weniger_geld(restaurant.kosten)
                    player1.hungry = 100
                    print(f'Du hattest ein saftiges Steak mit Ofenkartoffeln und Speckbohnen. Du fühlst dich herrlich, die Kosten in Höhe von {restaurant.kosten}€ wurden deinem Konto abgezogen')
                    print()
                    input('- weiter mit beliebiger Taste')
            elif eingabe_status1 == 3:
                if player1.money - (imbiss.kosten) < 0:
                    print(f'Leider genügt dein Guthaben nicht aus um die {imbiss.kosten}€ für den Imbiss zu zahlen.')
                    print()
                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                    trenner()
                else:
                    player1.weniger_geld(imbiss.kosten)
                    if player1.hungry <= 50:
                        player1.hungry += 50
                    else:
                        player1.hungry = 100
                    print(f'Du hattest eine Currywurst, Pommes mit Mayo. die Kosten in Höhe von {imbiss.kosten}€ wurden deinem Konto abgezogen')
                    print()
                    input('- weiter mit beliebiger Taste')
            elif eingabe_status1 == 4:
                if player1.money - (kiosk.kosten) < 0:
                    print(f'Leider genügt dein Guthaben nicht aus um die {kiosk.kosten}€ für den Kiosk zu zahlen.')
                    print()
                    input('- Weiter zum Hauptmenü mit beliebiger Taste -')
                    trenner()
                else:
                    player1.weniger_geld(kiosk.kosten)
                    player1.thursty = 100
                    print(f'Eine eiskalte Cola, das war genau das war du gebraucht hast... lecker! Die Kosten in Höhe von {kiosk.kosten}€ wurden deinem Konto abgezogen')
                    print()
                    input('- weiter mit beliebiger Taste -')
            elif eingabe_status1 == 5:
                player1.weniger_geld(zuhause.kosten)
                player1.health = 100
                print(f'Du hattest eine tolle Nacht in deinem Haus in Berlin.\nBei der Gelegenheit hast Du deine {zuhause.anzahl_zimmer} Zimmer geputzt. Die Mietein Höhe von {zuhause.kosten}€ wurden deinem Konto abgezogen.')
                print()
                input('- weiter mit beliebiger Taste -')
            else:
                eingabe_status = 'exit'





#%% ( 6 ) SPIEL BEENDEN

    elif eingabe_hauptmenue == 6:
        while True:
            print()
            print('###')
            print('ACHTUNG: Beim Beenden des Spiels werden keine Spielstände gespeichert.')
            print('')
            print('Bist Du sicher das du das Spiel beenden möchtest ?')
            print()
            print('( 1 ) Zurück zum Hauptmenü')
            print('( 2 ) Spiel beenden !')
            print()
            eingabe_beenden1 = input('Eingabe: ')
            if int(eingabe_beenden1) == 1:
                break
            elif int(eingabe_beenden1) == 2:
                game = 'exit'
                break
            else:
                print('Bitte nur 1 oder 2 eingeben')
    
print()
print('Vielen Dank fürs spielen, ich hoffe Du hattest Spaß')
input('Tippe eine beliebige Taste zum schließen')




