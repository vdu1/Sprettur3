import time #Importum module til að að hafa smá biðtíma milli falla og skipana

class Vikingur:
    #Svona ættu notendur að svara spurningunum
    answer_A = ["A", "a"]
    answer_B = ["B", "b"]
    answer_C = ["C", "c"]
    yes = ["J", "j", "Já", "já"]
    no = ["N", "n", "Nei", "nei"]

    #Hlutir sem notendur geta notfært sér
    snooz = 0

    rettinntak = ("\nNotaðu aðeins A, B, eða C\n") #Til að koma í veg fyrir misskilning
    jn = ("\nNotaðu aðeins já eða nei")

    def __init__(self):
        pass

    #Leið Víkings er brotin niður í mismunandi leiðir og byrjar í "inngangur"
    #Það þarf að laga byrjunina
    #time.sleep(1)
    def inngangur(self):
      teljari =0
      #time.sleep(5)
      print("Jæja, komið að Víkingi!")
      #time.sleep(2)
      print("\nÞitt verkefni er að vinna þig upp í gegnum lokaprófssögu Víkings og koma honum í gegnum prófin."
      " Passaðu þig að velja rétt, annars\nfellur Víkingur úr skólanu!")
      #time.sleep(5)
      print("\nNú byrjar ballið!")
      #time.sleep(3)
      print ("\nÞað er próf á morgun í Stærðfræðigreiningu II. Víkingur Goði var handviss um að hann gæti"
      " tekið þetta próf með bundið fyrir augun. Þess vegna mætti hann ekki fyrr en eftir miðnætti á"
      " næturvakt í VR-II. Þegar Víkingur sér hvað þetta er létt námsefni þá hugsar hann með sér að"
      " hann geti nú alveg eins sleppt því að læra.")
      #time.sleep(5)
      print("\nHvað gerir Víkingur næst?\n")
      #time.sleep(4)
      print ("""      A. Fer að spila surviv.io
      B. Fer að spila Fifa
      C. Hugsar með sér að það nægi að mæta vel seint í prófið""")
      choice = input("\n>>> ") #Here is your first choice.
      if choice in self.answer_A:
        #time.sleep(1)
        print ("\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
        " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n")
        teljari = self.prof()
      elif choice in self.answer_B:
        #time.sleep(1)
        print ("\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
        " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n")
        teljari = self.prof()
      elif choice in self.answer_C:
        #time.sleep(1)
        print ("\nGlæsilegt þú gast ekki klúðrað þessari spurningu því Stægrein II"
        " var svo létt fyrir Víking. Nú er Víkingur mættur í prófið.\nHvernig tekst hann á við prófið?\n")
        teljari = self.prof()
      else:
        print (self.rettinntak)
        self.inngangur()
      return teljari

    def prof(self):
      teljari = 0
      #time.sleep(1)
      print ("""      A. Biður um krassblað til að geta fínskrifað svörin sín
      B. Dritar niður á blað einhverju gáfulegu og fer út án þess að fara yfir
      C. Notar allan próftímann og reynir að krafsa í öll möguleg stig""")
      choice = input("\n>>> ")
      if choice in self.answer_A:
        #time.sleep(1)
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        teljari = self.prof()
      elif choice in self.answer_B:
        #time.sleep(1)
        print ("\nVíkingi leið ágætlega með prófið og langar að fagna. Leiðin liggur beint"
        " á Stúdentakjallarann.\nHvað fær Víkingur sér að borða?\n")
        teljari = self.matur()
      elif choice in self.answer_C:
        #time.sleep(1)
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        teljari = self.prof()
      else:
        print (self.rettinntak)
        teljari = self.prof()
      return teljari

    def matur(self):
      counter = 0
      #time.sleep(1)
      print ("""      A. Burger og bjór
      B. Grænmetislasagna
      C. Hnetusteik""")
      choice = input("\n>>> ")
      if choice in self.answer_A:
        #time.sleep(1)
        print ("\nÚff hvað burgerinn og bjórinn var góður! Víkingur er nú saddur"
        " og fer heim og leggur sig. Hann veit að síðasta lokaprófið er á morgun"
        " og það í tölvuteikningu. Hann er því harður við sjálfan sig og stillir"
        " vekjaraklukkuna aðeins eftir 3 tíma." #Henda time gæa hingað?
        " Tíminn líður, vekjaraklukkan hringir og Víkingi dauðbregður. Hann þarf nú að taka stóra ákvörðun."
        " Ýtir Víkingur á snooze.\nJá eða nei?")
        counter = self.logn()
      elif choice in self.answer_B:
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        counter = self.matur()
      elif choice in self.answer_C:
        print ("\nRangt, þú þekkir Víking greinilega ekki nógu vel. Reyndu aftur skepnan þín!\n")
        counter = self.matur()
      else:
        print (self.rettinntak)
        counter = self.matur()
      return counter

    #Það þarf að laga if setningar þannig að það komi ekki bull ef notandi slær inn vitlaust
    def logn(self):
      utskrifadir2 = 0
      #time.sleep(1)
      choice = input("\n>>> ")
      if choice in self.yes:
        snooz = 1 #Snoozar
      elif choice in self.no:
        snooz = 0 #Snoozar ekki
      else:
        print (self.jn)
        utskrifadir2 = self.logn()
      #time.sleep(1)
      print ("\nHvað gerir Víkingur eftir það?\n")
      #time.sleep(1)
      print ("""      A. Hann fer aftur að sofa
      B. Hann vaknar""")
      choice = input("\n>>> ")
      if choice in self.answer_A:
          if snooz > 0:
              #time.sleep(1)
              print ("\nÞað er rétt, Víkingur fór aftur að sofa"
              " EN sem betur fer ýtti hann á snooze, hann snoozar"
              " hins vegar of lengi en ekki nógu lengi til að geta ekki lært fyrir prófið."
              " Víkingur lærir uppí VR-II í alla nótt sem verður til þess að hann"
              " mætir of seint í tölvuteikningar lokaprófið daginn eftir.")
              utskrifadir2 = self.lokaprof()
          else:
              utskrifadir2 = 0
              #time.sleep(1)
              print ("\nÞað er rétt, Víkingur fór aftur að sofa."
              " Því miður gleymdi hann hins vegar að ýta á snooze og náði ekki"
              " að læra nóg fyrir tölvuteikningar lokaprófið."
              " Eins og svo oft áður þá varð svefninn Víkingi að falli"
              " og í þetta sinn sá svefninn til þess að Víkingur útskrifast ekki úr háskólanum! Hjálpaðu næsta"
              " nemanda að útskrifast\n")
      elif choice in self.answer_B:
        utskrifadir2 = 1
        #time.sleep(1)
        print ("\nÓtrúlegt en satt þá vaknar Víkingur á réttum tíma og hefur nægan tíma til að læra fyrir lokaprófið."
        " Hann mætir sáttur með T-stikuna í lokaprófið og rúllar því upp!")
        #time.sleep(1)
        print ("\nTil hamingju þú hefur náð að útskrifa Víking Goða!\n\nHjálpaðu næsta"
        " nemanda að útskrifast\n")
      else:
          print (self.rettinntak)
          self.logn()
      return utskrifadir2

    def lokaprof(self):
      #time.sleep(1)
      print ("\nVíkingur er mættur í prófið en þar sem að hann svaf svo yfir sig þá gleymdi hann T-stikunni heima."
      " Víkingur er í klípu, hvað gerir hann nú?\n")
      #time.sleep(1)
      print ("""      A. Hann fær lánað teikniborð frá Ara
      B. Hann ákveður að taka prófið fríhendis
      C. Hann vælir í kennaranum og fær að taka prófið í tölvu""")
      choice = input("\n>>> ")
      if choice in self.answer_A:
        utskrifadir2 = 1
        #time.sleep(1)
        print("\nVíkinur fékk lánað teikniborðið og rúllaði lokaprófinu upp.")
        #time.sleep(1)
        print("\nTil hamingju, þú náðir að útskrifa Víking Goða! Hjálpaðu næsta"
        " nemanda að útskrifast\n")
      elif choice in self.answer_B:
        utskrifadir2 = 0
        #time.sleep(1)
        print("\nVíkingur er því miður skelfilegur að teikna fríhendis.")
        #time.sleep(1)
        print("\nHann féll á prófinu og þar af leiðandi úr skólanum, því miður"
        " náður þú ekki að útskrifa Víking Goða!\n\nHjálpaðu næsta nemanda að útskrifast\n")
      elif choice in self.answer_C:
        utskrifadir2 = 1
        #time.sleep(1)
        print("\nVíkinur er frábær í Autocad og rúllar prófinu upp.")
        #time.sleep(1)
        print("\nTil hamingju, þú náðir að útskrifa Víking Goða! Hjálpaðu næsta"
        " nemanda að útskrifast\n")
      else:
        print (self.rettinntak)
        self.lokaprof()
      return utskrifadir2

def main():

    kall = Vikingur()
    inngangur = kall.inngangur()

if __name__ == "__main__":
    main()
