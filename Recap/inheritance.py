class fuel:
    def Petroleum(self):
        print("I use Disel\n")

class car(fuel):

    def creta(self):
        print("Creta: I'm a car")

    def Petroleum(self):
        print("I use Petrol\n")

class truck(fuel):

    def volvo(self):
        print("Volvo: I'm a truck")

c = car()
c.creta()
c.Petroleum()

t = truck()
t.volvo()
t.Petroleum()