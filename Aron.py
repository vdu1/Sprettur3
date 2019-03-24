# This Python file uses the following encoding: utf-8
import math
import random
import time #Importum module til að að hafa smá biðtíma milli spurninga

def get_input(output):
    return input(output)

def stor(spurning):
    tala = int(get_input(spurning))
    if tala >= 10:
        return 100
    else:
        return 50


class Aron:

    afangar = ["s", "l", "e"]
    skolar =["vi", "ví", "mr", "hr", "ms", "vma"]



    def __init__(self):
        pass

# Fall til að velja fyrsta endurtektarprófið

    time.sleep(1)
    def Velja1(self):
        namskeid1 = None
        time.sleep(1)
        print("Jæja komið að Aroni!\n")
        print("Þú féllst í þremur lokaprófum á fyrstu önninni þinni.\n"
        ' Nú verður þú að velja tvö námskeið til að taka í endurtekt.')
        time.sleep(1)

        while namskeid1 not in self.afangar:
            namskeid1 = input('\nS fyrir Stærðfræði greiningu, L fyrir Línulega Algebru eða E fyrir Eðlisfræði: ').lower()
            namskeid1 = namskeid1.lower()
            if namskeid1 in self.afangar:
                return namskeid1
            else:
                time.sleep(1)
                print("Það fór eitthvað úrskeiðis hjá þér reyndu aftur að velja námskeið")
                namskeid1 = None

# Fall til að velja seinna endurtektarprófið

    time.sleep(1)
    def Velja2(self, namskeid1):
        time.sleep(1)
        print("\nNú ertu búinn að velja eitt námskeið til að taka í endurtekt,"
        " próftaflan er heppileg svo þú getur tekið eitt endurtektarpróf í viðbót.\n")
        # Það er ekki hægt að velja sama endurtektarprófið tvisvar
        namskeid2 = None
        while namskeid2 not in self.afangar:

            if namskeid1.lower() =='s':
                namskeid2= input('L fyrir Línulega Algebru eða E fyrir Eðlisfræði: ')
            elif namskeid1.lower() =='l':
                namskeid2 = input('S fyrir Stærðfræði greiningu eða E fyrir Eðlisfræði: ')
            elif namskeid1.lower() =='e':
                namskeid2 = input('S fyrir Stærðfræði greiningu eða L fyrir Línulega Algebru: ')

            if namskeid2 in self.afangar:
                return namskeid2
            else:
                time.sleep(1)
                print("Það fór eitthvað úrskeiðis hjá þér reyndu aftur að velja námskeið")
                namskeid2 = None

# Fall sem er endurtektarpróf í Stærðfræðigreiningu 1

    time.sleep(1)
    def S1Prof(self):
        time.sleep(1)
        # Skilgreini þessar breytur sem núll til að geta notað þær seinna í forritinu
        StadFall =0
        einkunn =0
        TM =0
        print("\nÞú ert að læra fyrir endurtektarpróf í Stærðfræðigreiningu."
        " Þú hefur ekki mikinn tíma þar sem þú ert haugur.\n"
        'Þú verður að velja hvort þú viljir læra diffrun eða heildun fyrir prófið.\n')
        time.sleep(1)
        #Maður lærir hvort maður eyði tímanum sínum í að læra diffrun eða heildun, það er 50/50 hvort kemur.
        dh = None
        while dh != "d" and dh != "h":
            dh= input('Diffrun = D eða Heildun = H: ')
            dh = dh.lower()
        #Hérna fær maður að velja hversu mikið maður ætlar að sofa fyrir prófið, það fer eftir hvernig próf kennarinn gerir hvort það gagnist manni að sofa mikið
        time.sleep(1)
        svefn = 0
        while svefn <0.01:
            svefn = int(input("\nÞú ert illa undirbúinn en veist að svefn getur"
            " gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið? "))
        #Til þess að maður græði eitthvað á að læra fram eftir þá nær maður að læra um Taylor margliður ef maður lærir frameftir
        if svefn<4.5:
            time.sleep(1)
            print("\nÞú fórst svo seint að sofa að þú hafðir tíma til að læra"
            " Taylor margliður, vonandi kemur það á prófinu.\n")
            TM =1
        # 50/50 hvort það komi diffrun eða heildun, spurningin sem kemur verður 20% af prófinu
        DH=random.randint(0,1)
        time.sleep(1)
        if DH==1:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um Diffrun.\n')
            if dh.lower() == 'd':
                time.sleep(1)
                print('Þú ert heppinn, þú lærðir diffrun og hún kom á prófinu, einkunin þín hækkar um 2.\n')
                einkunn = einkunn +2
            elif dh.lower() == 'h':
                time.sleep(1)
                print("\nÞú valdir vitlaust, þú lærðir ekki diffrun og hún var"
                " 20% af prófinu, þú getur í mesta lagi fengið 8.\n")
            else:
                time.sleep(1)
                print("Þar sem þú valdir þú hvorugt áðan varst þú jafn týndur þegar þessi spurning kom og VD á B5.\n")

        if DH==0:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um heildun.\n')
            if dh.lower() == 'h':
                time.sleep(1)
                print('Þú ert heppinn, þú lærðir heildun og hún kom á prófinu, einkunin þín hækkar um 2.\n')
                einkunn = einkunn +2
            if dh.lower() == 'd':
                time.sleep(1)
                print("Þú valdir vitlaust, þú lærðir ekki heildun og hún var 20% af prófinu,"
                " þú getur í mesta lagi fengið 8.\n")
            else:
                time.sleep(1)
                print("Þar sem þú valdir þú hvorugt áðan varst þú jafn týndur þegar þessi spurning kom og VD á B5.\n")
        # 50/50 hvort Taylor margliður komi á prófinu. Ef maður lærði frameftir nær maður spurningunni rétt annars fær maður 0 stig.
        if random.randint(0,1)==1:
            time.sleep(1)
            print('Taylor margliður komu á prófinu.\n')
            if TM == 0:
                time.sleep(1)
                print('Þú hefðir kannski átt að vaka lengur til að læra Taylor margliður, þær voru 20% af prófinu.\n')
            if TM == 1:
                time.sleep(1)
                print('Vel gert að læra Taylor margliður, þú varst að ná auka 2 heilum á prófinu.\n')
                einkunn=einkunn + 2
        else:
            time.sleep(2)
            print('Taylor margliður komu ekki. Það kom fáranlegt markgildisdæmi sem þú áttir aldrei séns í. Óheppinn.\n')
        # Já eða nei spurning um hvort fall sé samfell
        # Gætum bætt við mynd af falli í næsta sprett til að hafa smá raunverulega stærðfræðigreiningu í þessu
        time.sleep(1)
        print('20% spurning hvort að fall sé samfellt á ákveðnu bili, Er það ekki bara já og nei spurning, eða 50/50...')
        svar = None
        while svar != "j" and svar != "j":
            svar = input('Er fallið samfellt eða ekki? J fyrir Já, N fyrir nei: ')
            svar = svar.lower()
        if random.randint(0,1)==1:
            rsvar = 'j'
            if svar.lower() == rsvar:
                time.sleep(2)
                print("\nVel gert, þú giskaðir rétt!\nÚtskýringin þín var"
                " samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt.\n")
                einkunn = einkunn + 1
            else:
                time.sleep(2)
                print('\nÞú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig.\n')
        else:
            rsvar= 'n'
            if svar.lower() == rsvar:
                tims.sleep(2)
                print('Vel gert, þú giskaðir rétt.\n'
                'Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt.\n')
                einkunn = einkunn + 1
            else:
                time.sleep(2)
                print('\nÞú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig.\n')
        # Hérna á að svara með tölustafnum 1
        time.sleep(2)
        print('Einfalt einingahringsdæmi, sem gildir 10%. Wu-hu.\n')
        SvarImba = 1
        Imba=int(input('cos^2(theta)+sin^2(theta)=x. Hvað er x? '))
        if Imba==SvarImba:
            time.sleep(2)
            print('\nVar þetta gisk? Það breytir engu, þetta var allavega rétt.\n')
            einkunn=einkunn+1
        else:
            time.sleep(2)
            print('Svona á að vita, þarna misstir þú dýrmætt stig úr pokanum.\n')
        # Hérna kemur svefninn inn. Ef maður fékk nægan svefn nær maður flóknu dæmi. Það er tilviljanakennt hversu mikinn svefn maður þarf.
        svefnkrafa = random.randint(0,9)
        if svefnkrafa >svefn:
            time.sleep(2)
            print("Þú hefðir átt að sofa meira. Benni kennari henti í svæsið"
            " 20% dæmi sem þú fattaðir ekki hvernig á að leysa.\n")
        if svefn >= svefnkrafa:
            einkunn= einkunn+2
            time.sleep(2)
            print('Vel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Benna.\n')
        # Það stendur á hverri blaðsíðu á EdBook quote eftir Douglas Adams
        time.sleep(2)
        print('Þetta er nú fáranleg 10% spurning.'
        ' Hver er uppáhalds rithöfundurinn hans Benna kennara?\n')
        time.sleep(2)
        print('A George R.R. Martin\n'
        'B Douglas Adams\n'
        'C Yrsa Sigurðardóttir\n')
        skrifa = None
        while skrifa != "a" and skrifa != "b" and skrifa != "c":
            skrifa=input('A, B eða C? ')
            skrifa = skrifa.lower()
        if skrifa.lower() == 'b':
            time.sleep(1)
            einkunn= einkunn +1
            time.sleep(2)
            print('\nÞú varst augljóslega duglegur að lesa EdBook yfir önnina.\n')
        else:
            time.sleep(1)
            print('Það þarf að lesa EdBook til að ná svona prófum.')
        #Prentum í lokin út lokaeinkunn og hvort viðkomandi hafi náð prófinu eða ekki
        time.sleep(2)
        print('Þú fékkst '+ str(einkunn) +' á prófinu.\n')
        if einkunn>4:
            time.sleep(2)
            print('Vel gert að ná prófinu, þú færð 6 einingar.\n')
            StadFall=1
        if einkunn<5:
            time.sleep(2)
            print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu.\n')
        return StadFall

# Fall sem er endurtektarpróf í Línulegri algebru

    #Setja mögulega 3 gæsa til að laga
    def Lprof(self):
        #Skilgreini þessar breytur hér til að geta notað þær seinna í forritinu
        StadFall =0
        einkunn =0
        EG =0
        # Þú velur hvort þú lærir og síðan er 50/50 hvort kemur á prófinu sem 20% spurning
        print('Þú ert að læra fyrir endurtektarpróf í Línulegri algebru. Þú hefur ekki mikinn tíma þar sem þú varst upptekinn í boltanum.\n'
        'Þú verður að velja hvort þú viljir læra Gauss eyðingu eða Fylkja margföldun.\n')
        time.sleep(1)
        gf = None
        while gf != "g" and gf != "f":
            gf= input('Gauss eyðingu = G eða Fylka margföldun = F: ')
            gf= gf.lower()
        #Hérna fær maður að velja hversu mikið maður ætlar að sofa fyrir prófið, það fer eftir hvernig próf kennarinn gerir hvort það gagnist manni að sofa mikið
        time.sleep(1)
        svefn = 0
        while svefn <0.01:
            svefn = int(input("\nÞú ert illa undirbúinn en veist að svefn getur"
            " gert gott fyrir þig, hvað ætlar þú að sofa mikið nóttinni fyrir prófið? "))# Maður verður að græða eitthvað á að læra frameftir. Í þessu tilfelli er það að geta leyst dæmi með eigin gildum
        if svefn<4.5:
            time.sleep(1)
            print('\nÞú fórst svo seint að sofa að þú hafðir tíma til að læra um Eigin gildi, vonandi kemur það á prófinu.\n')
            EG =1
        # Hér er valið tilviljanakennt hvort gauss eyðing eða fylkja margföldun komi á prófinu
        GF=random.randint(0,1)
        if GF==1:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um Gauss eyðingu.')
            if gf.lower() == 'f':
                time.sleep(1)
                print('Þú ert heppinn, þú lærðir Gauss eyðingu og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if gf.lower() == 'g':
                time.sleep(1)
                print('Þú valdir vitlaust, þú lærðir ekki Gauss eyðingu og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        if GF==0:
            time.sleep(1)
            print('Nú ertu mættur í prófið, fyrsta spurningin er um fylkja margföldun.')
            if gf.lower() == 'g':
                print('Þú ert heppinn, þú lærðir fylkja margföldun og hún kom á prófinu, einkunin þín hækkar um 2')
                einkunn = einkunn +2
            if gf.lower() == 'f':
                print('Þú valdir vitlaust, þú lærðir ekki fylkja margföldun og hún var 20% af prófinu, þú getur í mesta lagi fengið 8.')
        # Hérna er valið tilviljanakennt hvort eigin gildi sem sumir lærðu komi á prófinu
        # Ef maður lærði um eigin gildin fær maður +2 í einkunn
        if random.randint(0,1)==1:
            print('Eigin gildi komu á prófinu')
            time.sleep(1)
            if EG == 0:
                print('Þú hefðir kannski átt að vaka lengur til að læra Eigin gildi, þær voru 20% af prófinu')
            if EG == 1:
                print('Vel gert að læra Eigin gildi, þú varst að ná auka 2 heilum á prófinu')
                einkunn=einkunn + 2
        else:
            print('Þarna varstu óheppinn í staðinn fyrir eigin gildis dæmi komu 20% skilgreiningar sem þú bullaðir eitthvað í.')
            print('Röggi Möll sá í gegnum bullið þitt og gaf þér 0 stig fyrir dæmið')
        print('20% spurning hvort að fall sé línulegt')
        time.sleep(1)
        print('Er það ekki bara já og nei spurning, eða 50/50')
        # Hérna er 50/50 spurning hvort fallið sé línulegt
        # Gætum bætt við mynd af falli í næsta sprett til að hafa smá raunverulega línulega algebru í þessu
        svar = None
        while svar != "j" and svar != "j":
            svar = input('Er fallið línulegt eða ekki? J fyrir Já, N fyrir nei: ')
            svar = svar.lower()
        if random.randint(0,1)==0:
            rsvar = 'j'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        else:
            rsvar = 'n'
            if svar == rsvar:
                print('Vel gert, þú giskaðir rétt')
                print('Útskýringin þín var samt ekki nægilega góð svo þú færð bara helmingin af dæminu rétt')
                einkunn = einkunn + 1
            else:
                print('Þú giskaðir vitlaust og kunnir ekki nóg um efnið til að búa þér til stig')
        print('Einföld spurning, sem gildir 10%. Wu-hu.')
        #Hérna á að svara með Ákveða
        akveda=input('Hvað kallast Det(A) á Íslensku?')
        if akveda=='Ákveða' or akveda=='ákveða' or akveda=='Akveda' or akveda=='akveda':
            print('Var þetta gisk? Það breytir engu, þetta var allavega rétt')
            einkunn=einkunn+1
        else:
            print('Svona á að vita, þarna misstir þú dýrmætt stig úr pokanum')
        # Hérna kemur svefninn inn. Ef maður fékk nægan svefn nær maður flóknu dæmi. Það er tilviljanakennt hversu mikinn svefn maður þarf.
        svefnkrafa = random.randint(0,9)
        if svefnkrafa >svefn:
            print('Þú hefðir átt að sofa meira. Röggi Möll henti í svæsið 20% dæmi sem þú fattaðir ekki hvernig á að leysa.')
        if svefn >= svefnkrafa:
            einkunn= einkunn+2
            print('Vel gert, þú varst vel sofinn og fattaðir trixið í svæsnu 20% dæmi frá Rögga')
        #Þórður bróðir Rögnvalds kenndi okkur í Verzlunarskólanum svo okkur fannst tilvalið að hafa spurningu um hann
        print('Þetta er nú fáranleg spurning 10% spurning')
        print('Í hvaða framhaldsskóla kennir Þórður bróðir Rögnvalds stærðfræði?')
        print('Verzunarskóla Íslands')
        print('Menntaskólanum í Reykjavík')
        print('Leikskólanum í Skeifunni')
        print('Verkmenntaskólanum á Akureyri')
        print('Trúðaskólanum í Nauthólsvík')
        skrifa = None
        while skrifa not in self.skolar:
            skrifa=str(input('VÍ, MR, MS, VMA eða HR?'))
            skrifa = skrifa.lower()
        if skrifa.lower() == "ví" or skrifa.lower() == "vi":
            einkunn= einkunn +1
            time.sleep(1)
            print('Vel gert. Þú veist að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins')
        else:
            time.sleep(1)
            print('Ekki nógu gott, þú hefðir átt að vita að bræðurnir Möller myndu alltaf bara kenna í bestu menntastofnunum landsins.')
            print('Verzló er rétt svar')
        #Hérna prentast síðan niðurstöðurnar úr prófinu
        print('Þú fékkst '+ str(einkunn) +'á prófinu')
        if einkunn>4:
            time.sleep(1)
            print('Vel gert að ná prófinu, þú færð 6 einingar')
            StadFall=1
        if einkunn<5:
            time.sleep(1)
            print('Þú náðir ekki prófinu og ert kominn ennþá meira aftur úr í náminu')
        return StadFall
        #Setja mögulega 3 gæsa til að laga

#_main_
#Einingarnar byrja sem núll en ef maður nær tveimur prófum maður 12 einingar
def main():
    #Kallið
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

if __name__ == "__main__":
    main()
