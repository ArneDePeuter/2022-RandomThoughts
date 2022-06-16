import random

class Training:
    def __init__(self, groepsnaam, soort_training, opwarming, mid, cooldown):
        self.groepsnaam = groepsnaam
        self.opwarming = opwarming
        self.mid = mid
        self.cooldown = cooldown
        self.soort_training = soort_training
        self.maak_afstand = -self.opwarming-self.cooldown
        self.oefeningen = [self.generate_oefening("opwarming", self.opwarming),
                           self.generate_mid(),
                           self.generate_oefening("cooldown", self.cooldown)
                           ]

    def pick_oefening(self, file, gewenste_afstand):
        bestand = open(file)
        lines = bestand.readlines()
        mogelijke_oef = []
        for line in lines:
            if int(line[-5:].strip()) == gewenste_afstand: #laatste 5 char is de totale afstand
                mogelijke_oef.append(line)
        if len(mogelijke_oef)==0:
            return "NONE FOUND"
        else:
            return random.choice(mogelijke_oef)

    def generate_oefening(self, soort, afstand):
        oef = self.pick_oefening("{}.txt".format(soort),afstand)
        if type(afstand) != type:
            self.maak_afstand += afstand
        return oef

    def generate_mid(self):
        return [
                self.generate_oefening(self.soort_training, int),                       #aangezien elke afstand == int zal hij eender welke random oefening nemen
                self.generate_oefening(self.soort_training, self.mid-self.maak_afstand)
                ]

    def print(self):
        print("Groep {}: ".format(self.groepsnaam))
        print("Soort training: {}".format(self.soort_training))
        print('_________________________')
        print("{}: {}".format(1, self.oefeningen[0]))
        for i,oefening in enumerate(self.oefeningen[1]):
            print("{}: {}".format(i+2,oefening))
        print("{}: {}".format(4, self.oefeningen[2]))

C1_MA = Training("C1", "WC", 200, 1800, 200)
C1_MA.print()
