class Hyundai:

    def __init__(self, model, milage, color):
        self.model = model
        self.milage = milage
        self.color = color
        

    def displaySpec(self):
        print(f"{self.model}:\n{self.milage},\n{self.color}\n---\n")

car1 = Hyundai("Creta", 18, "White")
car2 = Hyundai("i20", 14, "Red")
car3 = Hyundai("Alcazar", 14, "White")

car1.displaySpec()
car2.displaySpec()
car3.displaySpec()