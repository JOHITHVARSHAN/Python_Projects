from abc import ABC, abstractmethod

# Abstract class
class Environment(ABC):
    @abstractmethod
    def pollution(self):
        pass

    def avg_speed(self):
        print("My Average speed is: 140 KM/Hrs\n")


class EVs(Environment):
    def pollution(self):
        print("I'm EVs, I am Pollution Free")

class Fuel_Vechile(Environment):
    def pollution(self):
        print("I'm FVs, I pollute the air")


evs = EVs()
FVs = Fuel_Vechile()

evs.pollution()
evs.avg_speed()
FVs.pollution()
FVs.avg_speed()
