import time

class Chrono:
    def __init__(self, aantal_zwemmers, aantal_meters):
        self.aantal_zwemmers = aantal_zwemmers
        self.aantal_meters = aantal_meters
        self.tijden = {}
        self.start = 0
        self.afgelegde_afstand = 0
        self.zwemmernr = 1

    # bij geen geregistreerde tijden start de chrono als er iemand afduwt
    def start_of_reset(self):
        if len(self.tijden) == 0:
            self.start = time.time()

    #functie om de tijden te kunnnen appenden bij de dict
    def append_time_to_dict(self, value):
        key = 'zwemmer {}'.format(self.zwemmernr)
        # Check if key exist in dict or not
        if key in self.tijden:
            if not isinstance(self.tijden[key], list):
                self.tijden[key] = [self.tijden[key]]
            self.tijden[key].append(value)
        else:
            self.tijden[key] = value

    #voegt lap tijd toe bij een gevraagd moment
    def lap(self):
        lap = time.time() - self.start
        print('zwemmer {}: {}'.format(self.zwemmernr, lap))
        self.append_time_to_dict(lap)

    # rollover als de 1e terug lapt en ook optellen van afstand
    def rollover(self):
        if self.zwemmernr > self.aantal_zwemmers:
            self.zwemmernr = 1
            self.afgelegde_afstand += 50
            print('Afgelegde afstand = {}'.format(self.afgelegde_afstand))

    # als de laatste zwemmer de gepaste afstand heeft afgelegd stopt het proces
    def stop(self,time):
        if self.afgelegde_afstand == self.aantal_meters and self.zwemmernr == self.aantal_zwemmers:
            time = False
        return time

    #verwerken van de tijden, elke zwemmer op t0 zetten en de 1e tijd verwijderen zodat geen nutteloze tijd wordt weergegeven
    def verwerk_tijden(self):
        self.zwemmernr = 1
        zwemmer_tijden_dict = {}
        for zwemmer in self.tijden.values():
            tijdlist = []
            for tijd in zwemmer:
                tijd -= zwemmer[0]
                if tijd != 0:
                    tijdlist.append(tijd)
            zwemmer_tijden_dict.update({'zwemmer {}'.format(self.zwemmernr) : tijdlist})
            self.zwemmernr+=1
        return zwemmer_tijden_dict

    #heel het process van de chronometer
    def process(self):
        time = True
        while time:
            actie = str(input('Geefactie: '))
            if actie == 'duw':
                self.start_of_reset()
                self.rollover()
                time = self.stop(time)
                self.lap()
                self.zwemmernr += 1

        self.tijden = self.verwerk_tijden()
        return self.tijden

def main():
    cr1 = Chrono(2, 100)
    print(cr1.process())

if __name__ == '__main__':
    tijden = main()