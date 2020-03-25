class vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(vehicle):
    def sayHello(self):
        print("Hello World")

class Van(vehicle):
    pass

class Pikup(vehicle):
    pass

class Estatecar(vehicle):
    pass

car_1 = Car()
car_1.turnOnAirConditioner()

van_1 = Van()
van_1.turnOnAirConditioner()

pikup_1 = Pikup()
pikup_1.turnOnAirConditioner()

estatecar_1 = Estatecar()
estatecar_1.turnOnAirConditioner()