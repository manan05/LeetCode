class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.sys = {}
        self.sys[1] = big
        self.sys[2] = medium
        self.sys[3] = small

    def addCar(self, carType: int) -> bool:
        if(carType == 1):
            if(self.sys.get(1) > 0):
                self.sys[1] -= 1
                return True
            else:
                return False
        elif(carType == 2):
            if(self.sys.get(2) > 0):
                self.sys[2] -= 1
                return True
            else:
                return False
        else:
            if(self.sys.get(3) > 0):
                self.sys[3] -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)