import time



start = False
def ontgrendel(pogingen,wachtwoord):
    while True:
        while pogingen > 0 :
            a = input("Gelieve het wachtwoord in te voeren. ")
            if a==wachtwoord:
                print("wachtwoord correct")
                time.sleep(1)
                start = True
                return True
            else:
                pogingen = pogingen - 1
                print("Dit wachtwoord is fout. Je hebt nog ",pogingen," pogingen")
        print("Te veel foute poingen. Je kan niet inloggen voor 30sec.")
        for i in range(6):
            print("nog ", 30 - (i * 5), " seconden.")
            for k in range(5):
                time.sleep(1)

        pogingen=pogingen+1

ontgrendel(3,"Kyrill is geweldig!")
