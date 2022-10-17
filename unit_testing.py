import unittest
from main import Car, Engine


class TestCar(unittest.TestCase):
    def test_can_move (self):
        test_car = Car(Engine(100, 'Ferrari'), 100, False, 4)
        actual = test_car.can_move()
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()