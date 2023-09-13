import unittest
from car import Car, Motorcycle, Vehicle  # Replace with the actual module where your classes are defined

class TestCar(unittest.TestCase):

    def test_instance_of_vehicle(self):
        car = Car("Company", "Model", 2023)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car, Vehicle)  # Assuming Vehicle is the base class

    def test_car_has_4_wheels(self):
        car = Car("Company", "Model", 2023)
        self.assertEqual(car.numWheels, 4)

    def test_car_speed_after_test_drive(self):
        car = Car("Company", "Model", 2023)
        car.testDrive()
        self.assertEqual(car.speed, 60)

    def test_car_stops_after_park(self):
        car = Car("Company", "Model", 2023)
        car.testDrive()
        car.park()
        self.assertEqual(car.speed, 0)

class TestMotorcycle(unittest.TestCase):

    def test_instance_of_vehicle(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        self.assertIsInstance(motorcycle, Motorcycle)
        self.assertIsInstance(motorcycle, Vehicle)  # Assuming Vehicle is the base class

    def test_motorcycle_has_2_wheels(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        self.assertEqual(motorcycle.numWheels, 2)

    def test_motorcycle_speed_after_test_drive(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        motorcycle.testDrive()
        self.assertEqual(motorcycle.speed, 75)

    def test_motorcycle_stops_after_park(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        motorcycle.testDrive()
        motorcycle.park()
        self.assertEqual(motorcycle.speed, 0)

if __name__ == '__main__':
    unittest.main()
