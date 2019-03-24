# This Python file uses the following encoding: utf-8
import math
import random
import time

class Hrolfur:

    def __init__(self):
        pass

    def intro(self):
        counter =0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]

        print("Hrólfur Sveinsson er ungur drengur úr Hafnarfirðinum."+"\n")
        time.sleep(1)
        print("Hrólfur á við ýmis vandamál að stríða. Útaf þessum vandamálum er hann oft áhyggjufullur."+"\n")
        time.sleep(1)
        print("Þökk sé streitu sér Hrólfur ungur að hann er nálægt því að missa hárið."+"\n")
        time.sleep(1)
        print("Þú ert nú komin í það hlutverk að hjálpa Hrólf með allar ákvarðanir til að minnka streitu og halda í hárið."+"\n")
        time.sleep(1)
        print("Hrólfur veit að ef hann missir allt hárið þá mun hafa ekki hafa sjálfstraustið í að klára háskólann."+"\n")
        time.sleep(1)
        print("Fyrsta stóra ákvörðunin sem þú þarft að hjálpa Hrólf með er í hvaða framhaldsskóla hann á að fara.")
        time.sleep(1)
        print ("""  A. Menntaskólann í Reykjavík
        B. Flensborgarskólann í Hafnarfirði
        C. Verzlunarskóla Íslands""")
        choice = input(">>> ") #Here is your first choice.
        if choice in svar_A:
            print("Jæja, þú ert ömurlegur ráðgjafi. Hrólfur missti allt hárið og féll úr MR á fyrstu önninni. Hann er samt mjög ánægður á dælunni.")
            return 100
        elif choice in svar_B:
            counter += self.option_Flens()
        elif choice in svar_C:
            counter += self.option_Verzl()
        else:
            print ("A, B eða C takk fyrir")
            self.intro()
        return counter

    def option_Flens(self):
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]

        print("Hrólfur er mættur í Flensborg. Honum líður vel í Firðinum og rúllar upp náminu."+"\n")
        print("Þrátt fyrir að vera heimakær hefur Hrólfur áhyggjur af að finna ekki spennandi kvenkost í Hafnarfirðinum."+"\n")
        print("Þetta angrar hann ekki svakalega en samt nóg til að hann missi 4 hár af hausnum"+"\n")
        counter = 4
        time.sleep(1)
        print("Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum"+"\n")
        print("Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n")
        print("Hrólfur veit samt að það er mikið álag að vera í meistaraflokki"+"Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League"+"\n")
        time.sleep(1)
        print (" A. FH  "
        "B. Passion League ")
        choice = input(">>> ")
        if choice in svar_A:
            print("Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár")
            counter += 10
        elif choice in svar_B:
            print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
        else:
            print ("A eða B koma svo")
        print("Námið í Flensborg er að fara vel með Hrólf. Hann er samt að velta því fyrir sér hvort hann eigi að eltast við að vera Dúx."+"\n")
        print("Það gæti gert eitthvað fyrir sjálfstraustið hans að vera dúx en það er auðvitað mikil vinna sem myndi fara í það"+"\n")
        print("A fyrir að eltast við að vera dúx eða B fyrir að útskrifast bara")
        time.sleep(1)
        choice = input(">>> ")
        if choice in svar_A:
            print("Ekki vera svona heimskur, maður græðir ekkert á að vera Dúx, spurðu bara Erni Jónsson"+"\n")
            print("-10 hár fyrir óþarfa metnað í námi")
            counter += 10
        elif choice in svar_B:
            print ("Hrólfur nýtur sín vel í náminu þar sem hann var ekki að eltast við einkunnir. Hann lærir efnið vel og missir ekkert hár."+"\n")
        else:
            print ("A eða B koma svo")
        print("Hrólfur útskrifaðist úr Flensborg og stefnir núna á Iðnaðarverkfræði við Háskóla Íslands")
        return counter



    def option_Verzl(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]

        print("Hrólfur er mættur í Verzló. Honum finnst félagslífið skemmtilegt en námið er erfitt."+"\n")
        print("Snappið hans Hrólfs er ekki lengi að fyllast af skonsum eftir að hann byrjar í Verzló."+"\n")
        print("Álagið við að svara öllum þessum skonsum lætur hann missa 10 hár af hausnum"+"\n")
        counter += 10
        time.sleep(1)
        print("Hrólfur er mikill fótboltastrákur. Hann elskar fátt meira en að sparka í boltann með góðum félögum"+"\n")
        print("Hrólfur er hinsvegar í erfiðri stöðu. Félagarnir eru ekki með jafn mikið metnað í boltanum. Hrólfur sjálfur gæti fengið að æfa með meistaraflokki FH í sumar."+"\n")
        print("Hrólfur veit samt að það er mikið álag að vera í meistaraflokki"+"Ætti hann að eltast við draumana í FH eða ætti hann að fara með félögunum í Passion League"+"\n")
        time.sleep(1)
        print ("""  A. FH
        B. Passion League
        """)
        choice = input(">>> ")
        if choice in svar_A:
            print("Þetta var slæm ákvörðun. Hrólf líður ekki vel í FH reynir í nokkra mánuði að æfa undir miklu álagi en hættir síðan. -10 hár")
            counter = counter -10
        elif choice in svar_B:
            print ("Geggjuð ákvörðun. Hrólfur skemmtir sér konunglega með félögunum í Passion League, einn stóran Tuborg takk."+"\n")
        else:
            print ("A eða B koma svo")
        print("Námið í Verzló er erfitt fyrir Hrólf. Hann er að velta því fyrir sér hvort hann eigi að halda áfram eða hætta bara í skólanum."+"\n")
        print("Hann gæti átt erfitt með að halda sér í Verzló en það gæti verið að hann flosni úr skóla ef hann fer í Flensborg"+"\n")
        print("A fyrir að halda áfram eða B fyrir Flensborg")
        time.sleep(1)
        choice = input(">>> ")
        if choice in svar_A:
            print("Hrólfur tók sig á fyrir prófin og gekk mjög vel. Hann var alltaf vel undirbúinn og var því ekkert stressaður"+"\n")
        elif choice in svar_B:
            print ("Hrólfur fílaði sig ekki alveg í Flensborg, flosnaði úr námi og fór aldrei í háskólann."+"\n")
            counter =100
            return counter
        else:
            print ("A eða B koma svo")
        print("Hrólfur útskrifaðist úr Verzlunarskólanum og stefnir núna á Iðnaðarverkfræði við Háskóla Íslands"+"\n")
        return counter


    def HaskoliStart(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        print("Nú er Hrólfur mættur í háskólann eftir fína framhaldsskólagöngu"+"\n")
        time.sleep(1)
        print("Hrólfur fattar strax að hann eigi ekki efni á kaupa sér hádegismat alla daga"+"\n")
        time.sleep(1)
        print("A - Á Hrólfur að læra að gera sér nesti eða "+"\n")
        print("B - Finna sér kærustu til að gera nestið fyrir sig alla daga? "+"\n")
        choice = input(">>> ")
        if choice in svar_A:
            counter += self.HaskoliA()
        elif choice in svar_B:
            counter += self.HaskoliB()
        else:
            self.HaskoliStart()
        return counter

    def HaskoliA(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]
        time.sleep(1)
        print("Hrólfur lærði að gera nesti, hann missir hinsvegar smá svefn við að vakna alltaf til að gera nesti"+"\n")
        print("Mínus 5 hár útaf svefnleysi"+"\n")
        counter += 5
        time.sleep(1)
        print("Hrólf gengur vel í náminu á fyrstu önn, hann þarf að fara í eitt endurtektarpróf en pakkar því saman"+"\n")
        print("Á annarri önninni trúðar Hrólfur oft yfir sig á djamminu"+"\n")
        time.sleep(1)
        print("Á Hrólfur að hætta að drekka eins og T-Paul vinur hans?")
        choice1 = input(">>> ")
        if choice1 in Ja:
            print("Slæm ákvörðun, þar sem Hrólfur getur ekki slakað á um helgar með félögunum og einn skíítkaldan missir hann 20 hár")
            counter += 20
        if choice1 in Nei:
            print("Góð ákvörðun, þrátt fyrir að Hrólfur prjónaði stundum yfir sig þá getur hann slakað vel á um helgar með félögunum"+"\n")
            print("Hann þarf samt oft að hafa áhyggjur eftir að hafa trúðað yfir sig og missir því 5 hár")
            counter += 5
        time.sleep(1)
        if choice1 in Ja:
            print("Þrátt fyrir að vera hættur að drekka þá nær Hrólfur öllum prófunum á önn númer 2"+"\n")
        if choice1 in Nei:
            print("Hrólfur náði öllum prófunum og fagnaði proflokunum vel á b5"+"\n")
        print("Á önn númer 3 fattar Hrólfur að hann þurfi að finna sér kærustu"+"\n")
        time.sleep(1)
        print("Þrjár stelpur reyna við hann, allar eru með frábæran hlátur en hverja á hann að velja?"+"\n")
        print("A - Hressa sveitastelpu sem hatar ekki sopann"+"\n")
        print("B - Verzló skvísu af nesinu"+"\n")
        print("C - Hávaxinn fótboltatöffara úr Hlíðunum"+"\n")
        choice2 = input(">>> ")
        time.sleep(1)
        if choice2 in svar_A:
            print("Þið djammið mikið saman og skemmtið ykkur vel"+"\n")
            print("Of mikið myndu sumir segja og hann missir 10 hár"+"\n")
            counter += 10
        if choice2 in svar_B:
            print("Einbeitingin hverfur smá frá náminu og það veldur einhverjum áhyggjum"+"\n")
            time.sleep(1)
            print("Í staðinn fær Hrólfur að sofa aðeins lengur því nú fær hann nesti tilbúið af Nesinu"+"\n")
            print("Mínus 5 hár samt fyrir að missa einbeitingu frá náminu")
            print("Þetta gengur vel en auðvitað eru einhverjir hnökkrar og Hrólfur missir samtals 5 hár")
            counter += 5
        if choice2 in svar_B:
            print("Þetta gengur vel en auðvitað eru einhverjir hnökkrar og Hrólfur missir samtals 5 hár")
            counter += 5
        if choice2 in svar_C:
            print("Þetta gengur vel en auðvitað eru einhverjir hnökkrar og Hrólfur missir samtals 5 hár")
            counter += 5
        if choice2 in svar_C:
            print("Fótboltatöffararnir njóta sín vel. Það þarf oftar að skipta um kodda en áhyggjurnar á heimilinu er almennt litlar"+"\n")
            counter += 0
        print("Á önn númer þrjú eru 4 auðveldir áfangar sem Hrólfur þarf ekki að hafa neinar áhyggjur af"+"\n")
        time.sleep(1)
        print("Hrólfur þarf samt líka að taka áfangann Verkefnastjórnun, áfanginn er gríðarlega erfiður og þarf mikla vinnu til að ná honum"+"\n")
        print("Hvaða einkunn stefnir Hrólfur á að fá í áfanganum, því meiri vinnu sem hann leggur í áfangann því hærri einkunn en hármissir í staðin."+"\n")
        verk = int(input(">>>"))
        time.sleep(1)
        if verk*0==0:
            counter += (verk-5)*5
        else:
            print("Reyndu aftur"+"\n")
            print("Þú þarft að slá inn tölu"+"\n")
            verk = int(input(">>>"))
            counter += (verk-5)*5
        print("Það var stressandi að fá góða einkunn í verkefnastjórnun, Hrólfur missti 5 hár fyrir hverja einkunn sem hann fékk yfir 5"+"\n")
        print("Hvaða einkunn stefnir Hrólfur á að fá í áfanganum, því meiri vinnu sem hann leggur í áfangann því meira hár missir hann"+"\n")
        verk = int(input())
        counter += (verk-5)*4
        print("Það var stressandi að fá góða einkunn í verkefnastjórnun, Hrólfur missti 4 hár fyrir hverja einkunn sem hann fékk yfir 5"+"\n")
        time.sleep(1)
        print("Hrólfur fer hlægjandi í gegnum önn 4 og 5"+"\n")
        time.sleep(2)
        print("Fyrir seinustu önnina gerði Hrólfur stór mistök."+"\n")
        print("Hann tók sömu valáfanga og Lexi"+"\n")
        print("Nú er hann kominn í þá gríðarlega erfiðu stöðu að þurfa að ná þessum námskeiðum"+"\n")
        print("Við það að reyna að ná þessum fáranlegu námskeiðum sem Lexi valdi missti Hrólfur 10 hár, vonandi átti hann efni á því"+"\n")
        counter +=10
        return counter

    def HaskoliB(self):
        counter=0
        svar_A = ["A", "a"]
        svar_B = ["B", "b"]
        svar_C = ["C", "c"]
        Ja = ["J", "j", "já", "JÁ", "Já"]
        Nei = ["N", "n", "nei", "Nei", "NEI"]
        time.sleep(1)
        print("Hrólfur er alltaf vel nærður og missir engin hár á fyrstu önninni"+"\n")
        time.sleep(1)
        print("Hrólf gengur vel í náminu á fyrstu önn, hann þarf að fara í eitt endurtektarpróf en pakkar því saman"+"\n")
        print("Á annarri önninni trúðar Hrólfur oft yfir sig á djamminu"+"\n")
        time.sleep(1)
        print("Á Hrólfur að hætta að drekka eins og T-Paul vinur hans?")
        choice1 = input(">>> ")
        if choice1 in Ja:
            print("Slæm ákvörðun, þar sem Hrólfur getur ekki slakað á um helgar með félögunum og einn skíítkaldan missir hann 20 hár")
            counter += 20
        if choice1 in Nei:
            print("Góð ákvörðun, þrátt fyrir að Hrólfur prjónaði stundum yfir sig þá getur hann slakað vel á um helgar með félögunum"+"\n")
            print("Hann þarf samt oft að hafa áhyggjur eftir að hafa trúðað yfir sig og missir því 5 hár")
            counter += 5
        time.sleep(1)
        if choice1 in Ja:
            print("Þrátt fyrir að vera hættur að drekka þá nær Hrólfur öllum prófunum á önn númer 2"+"\n")
        if choice1 in Nei:
            print("Hrólfur náði öllum prófunum og fagnaði proflokunum vel á b5"+"\n")
        print("Á önn númer 3 eru 4 auðveldir áfangar sem Hrólfur þarf ekki að hafa neinar áhyggjur af"+"\n")
        time.sleep(1)
        print("Hrólfur þarf samt líka að taka áfangann Verkefnastjórnun, áfanginn er gríðarlega erfiður og þarf mikla vinnu til að ná honum"+"\n")
        print("Hvaða einkunn stefnir Hrólfur á að fá í áfanganum, því meiri vinnu sem hann leggur í áfangann því meira hár missir hann"+"\n")
        verk = int(input(">>>"))
        counter += (verk-5)*5
        verk = int(input())
        counter += (verk-5)*4
        print("Það var stressandi að fá góða einkunn í verkefnastjórnun, Hrólfur missti 4 hár fyrir hverja einkunn sem hann fékk yfir 5"+"\n")
        time.sleep(1)
        print("Hrólfur fer hlægjandi í gegnum önn 4 og 5"+"\n")
        time.sleep(2)
        print("Fyrir seinustu önnina gerði Hrólfur stór mistök."+"\n")
        print("Hann tók sömu valáfanga og Lexi"+"\n")
        print("Nú er hann kominn í þá gríðarlega erfiðu stöðu að þurfa að ná þessum námskeiðum"+"\n")
        print("Við það að reyna að ná þessum fáranlegu námskeiðum sem Lexi valdi missti Hrólfur 10 hár, vonandi átti hann efni á því"+"\n")
        counter +=10
        return counter


    def Nidurstada(self, x):
        print("Nú er Hrólfur búinn með skólann")
        print("Hann endaði með "+str(x)+"hár eftir á kollinum")
        if x>50:
            print("Þarf sem Hrólfur átti meira en 20 hár eftir á hausnum þá hafði hann nóg sjálfstraust til að klára dæmið og útskrifaðist"+"\n")
            return 1
        if x <= 50:
            print("Þarf sem Hrólfur missti of mikið hár gat hann ekki náð að klára dæmið, þú náðir ekki að útskrifa Hrólf\n")
            return 0

def main():
    kall = Hrolfur()
    har = 100
    har -= kall.intro()
    if har>20:
        har -= kall.HaskoliStart()
    kall.Nidurstada(har)

if __name__ == "__main__":
    main()
