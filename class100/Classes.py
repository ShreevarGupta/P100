class Car(object):
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def start(self): 
        print("It started.")
    
    def gearChange(self):
        print("It changed its gear.")

def main():
    Toyota = Car("Name - Fortuner", "Color - Brown", "Model - 2000")
    print(Toyota.name)
    print(Toyota.color)
    print(Toyota.model)
    Toyota.start()

    Maruti_Suzuki = Car("Name - Maruti Ciaz", "Color - White", "Model - 2016")
    print(Maruti_Suzuki.name)
    print(Maruti_Suzuki.color)
    print(Maruti_Suzuki.model)
    Maruti_Suzuki.gearChange()

main()
