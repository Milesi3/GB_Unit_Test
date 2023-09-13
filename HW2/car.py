from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, company, model, yearRelease):
        self.company = company
        self.model = model
        self.yearRelease = yearRelease
        self.numWheels = 0
        self.speed = 0

    @abstractmethod
    def testDrive(self):
        pass

    @abstractmethod
    def park(self):
        pass

class Car(Vehicle):
    def __init__(self, company, model, yearRelease):
        super().__init__(company, model, yearRelease)
        self.numWheels = 4

    def testDrive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

class Motorcycle(Vehicle):
    def __init__(self, company, model, yearRelease):
        super().__init__(company, model, yearRelease)
        self.numWheels = 2

    def testDrive(self):
        self.speed = 75

    def park(self):
        self.speed = 0
