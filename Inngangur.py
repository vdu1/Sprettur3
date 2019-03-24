class Inngangur: #Klasinn

    def __init__(self): #Smiðurinn, notum engan "smið" eins og er, eða hvað?
        pass

    def inngangur(self): #Fallið sem byrjar leikinn
        #time.sleep(1)
        print("\nAllir nemendur við Háskóla Íslands glíma við sín eigin vandamál og þurfa þeir að leysa þau ef"
        " þeir ætla að útskrifast með sæmd úr\nháskólanum. Þitt verkefni er að komast í gegnum þrautir leiksins og ná að brautskrá sem flesta nemendur.")
        #time.sleep(5)
        print("\nHefjumst handa!")
        #time.sleep(1)
        nafn = input("\nNafnið þitt er? ")
        #time.sleep(2)
        print("\nJæja " + nafn + ", þitt fyrsta verkefni er Viktor!\n")
        return nafn
def main():
    kall = Inngangur()
    nafn1=kall.inngangur()

if __name__ == "__main__":
    main()
