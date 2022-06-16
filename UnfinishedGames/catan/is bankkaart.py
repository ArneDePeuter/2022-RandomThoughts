bankkaart = int(input('Geef bankkaart: '))
getal = int(str(bankkaart)[0:-2])
laatste_getal = str(bankkaart)[-2:]

if str(getal % 97) == str(bankkaart)[-2:]:
    print('is een bankkaart')

