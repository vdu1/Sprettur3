# This Python file uses the following encoding: utf-8
import time #Importum module til að að hafa smá biðtíma milli falla og skipana
from Viktor import Viktor #Importum Viktor úr Viktornyjasti til að geta kallað á leikinn í inngangsforritinu
from Vikingur import Vikingur #Importum Vikingur úr Vikingurnyjasti til að geta kallað á leikinn í inngangsforritinu
from Hrolfur import Hrolfur #Importum Hrolfur úr LeikurHrólfur til að geta kallað á leikinn í inngangsforritinu
from Aron import Aron #Importum Aron úr Aronnyjasti til að geta kallað á leikinn í inngangsforritinu
from Inngangur import Inngangur

#__main__
def main():
    Teljari = 0

    kall = Inngangur()
    nafn1=kall.inngangur()

#Kallið fyrir leikur1
    kall = Viktor()
    kall.Kynning()
    spurningar = [("Fílar Viktor hávaða? (Já/Nei):", "Nei"),
        ("Fílar Viktor að tala? (Já/Nei):", "Nei"),
        ("Elskar Viktor þögnina? (Já/Nei):", "Já"),
        ("Hvað er uppáhaldsdrykkurinn hans Viktors? (Coke Zero/Peru Nocco/Hvítur GoGo/Pepsi Max):", "Pepsi Max"),
        ("Hvernig bíl á Vikki D? (Trabant/Lada Sport/Audi/Passat)", "Audi"),
        ("Hvað á Viktor margar klippingar eftir? (0/3 max/1/∞):", "3 max"),
        ("Hvað er uppáhalds tækjavörumerkið hans Viktors? (Apple/Dell/HP/Denver):", "Apple"),
        ("Hver er besti hópfélagi Viktors? (Hrólfur/Aron/Þorgeir/Víkingur):", "Þorgeir"),
        ("Bjó Vikki D til iPad gryfjuna? (Já/Nei/Ekki Lexi):", "Já"),
        ("Hvað er prófælmyndin hans Viktors gömul? (2 vikna/3 mánaða/6 ára/Á ekki facebook):", "6 ára")
        ]
    i=0
    counter =0
    for spurning, rettsvar in spurningar:
        i += 1
        if kall.spyrja(spurning, rettsvar, i)is True:
            counter += 1

    Teljari += kall.nidurstada(counter, len(spurningar))

    #Kallið fyrir leikur2
    kall = Vikingur()
    Teljari += kall.inngangur()

    #Kallið fyrir leikur3
    einingar=0
    kall = Aron()
    namskeid1 = kall.Velja1()
    namskeid2 = kall.Velja2(namskeid1)
    if namskeid1.lower() == 's' or namskeid2.lower() == 's':
        einingar = einingar+6*kall.S1Prof()

    # Til að spara forritun átti maður ekki séns á að ná eðlisfræðinni
    # Bætum mögulega við prófi í eðlisfræði fyrir næsta sprett
    if namskeid1.lower() == 'e' or namskeid2.lower() == 'e':
        print('Aldeilis mistök sem þú gerðir að velja Eðlisfræði prófið.')
        print('Þú áttir aldrei séns og fékkst núll í prófinu')

    if namskeid1.lower() == 'l' or namskeid2.lower() =='l':
        einingar = einingar+6*kall.Lprof()
    print('Þú endaðir með '+ str(einingar) + " einingar, til hamingju! Hjálpaðu næsta nemanda að útskrifast")
    if einingar == 12:
        Teljari += 1

    #Kallið fyrir leikur4
    kall = Hrolfur()
    har = 100
    har -= kall.intro()
    if har>20:
        har -= kall.HaskoliStart()
    Teljari += kall.Nidurstada(har)

    #Nú viljum við taka allt saman til að birta niðurstöður leikjanna
    print(nafn1 + " þú útskrifaðir " + str(Teljari) + " af 4 nemendum")

if __name__ == "__main__":
    main()
