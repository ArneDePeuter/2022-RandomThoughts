import time

class Chrono:
    def __init__(self, aantal_zwemmers, aantal_meters, ad_tijd):
        self.aantal_zwemmers = aantal_zwemmers
        self.aantal_meters = aantal_meters
        self.ad_tijd = ad_tijd
        self.tijden = {}

    def set_aantal_zwemmers(self, new_aantal_zwemmers):
        self.aantal_zwemmers = new_aantal_zwemmers

    def set_aantal_meters(self, new_aantal_meters):
        self.aantal_meters = new_aantal_meters

    def set_reset_tijden_and_afstanden(self):
        for zwemmers in range(self.aantal_zwemmers):
            self.tijden["Zwemmer {} tijden: ".format(zwemmers+1)] = None

    def starten(self, starten, aantalgeduwd):
        while starten:
            ingave = str(input("Geef input: "))
            if ingave == 'duw':
                aantalgeduwd +=1
                if aantalgeduwd == 1:
                    start = time.time()
                end = time.time()
                time_elapsed = end-start
                self.tijden["Zwemmer {} tijden: ".format(aantalgeduwd)] = time_elapsed
            if aantalgeduwd == self.aantal_zwemmers:
                starten = False
        return start, starten

    def banen(self,start):
        for lap_or_finish in range(round(self.aantal_meters/50)):
            print("Na {} meter: ".format((lap_or_finish+1)*50))
            aantal_geduwd = 0
            for zwemmers in range(self.aantal_zwemmers):
                ingave = str(input('Geef input: '))
                if ingave == 'duw':
                    aantal_geduwd += 1
                    end = time.time()
                    time_elapsed = end - start

                    tijdlist = []
                    for tijd in self.tijden["Zwemmer {} tijden: ".format(zwemmers+1)]:
                        tijdlist.append(tijd)
                    tijdlist.append(time_elapsed)

                    self.tijden.update({"Zwemmer {} tijden: ".format(aantal_geduwd): tijdlist})

    def verwerktijden(self):
        for zwemmer in range(self.aantal_zwemmers):
            tijden = self.tijden["Zwemmer {} tijden: ".format(zwemmer+1)]
            print(tijden[0])


def main():
    chronometer = Chrono(2,100, False)
    chronometer.set_reset_tijden_and_afstanden()
    print(chronometer.tijden)

    starten = True
    aantalgeduwd = 0

    start, starten = chronometer.starten(starten, aantalgeduwd)
    print(chronometer.tijden)
    chronometer.banen(start)
    print(chronometer.tijden)
    chronometer.verwerktijden()



if __name__ == '__main__':
    main()