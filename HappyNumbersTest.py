import random
import unittest
import HappyNumbers

class SimpleHappyTests(unittest.TestCase):
    def test_1_is_always_happy(self):
        self.assertEquals(True, HappyNumbers.is_happy(1, list()))

    def test_2_3_4_5_6_8_9_are_not_happy(self):
        """
        2,3,4,5,6,8,9 are all unhappy numbers
        """
        numbers = [2,3,4,5,6,8,9]
        for num in numbers:
            self.assertEquals(False, HappyNumbers.is_happy(num, list()))

    def test_7_is_happy(self):
        self.assertEquals(True, HappyNumbers.is_happy(7, list()))

    def test_powers_of_10_are_happy(self):
        """
        all powers of 10 are happy
        """
        for power in range(1,10):
            number = pow(10,power)
            self.assertEquals(True, HappyNumbers.is_happy(number, list()))

class DictHappyTests(unittest.TestCase):
    def test_1_is_always_happy(self):
        self.assertEquals(True, HappyNumbers.is_happy_dict(1, list()))

    def test_2_3_4_5_6_8_9_are_not_happy(self):
        """
        2,3,4,5,6,8,9 are all unhappy numbers
        """
        numbers = [2,3,4,5,6,8,9]
        for num in numbers:
            self.assertEquals(False, HappyNumbers.is_happy_dict(num, list()))

    def test_7_is_happy(self):
        self.assertEquals(True, HappyNumbers.is_happy(7, list()))

    def test_powers_of_10_are_happy(self):
        """
        all powers of 10 are happy
        """
        for power in range(1,10):
            number = pow(10,power)
            self.assertEquals(True, HappyNumbers.is_happy_dict(number, list()))

    def test_check_random_numbers(self):
        for i in range(1,10):
            number = random.randint(1,100)
            self.assertEquals(HappyNumbers.is_happy(number,list()), HappyNumbers.is_happy_dict(number, list()))

class QuickHappyTests(unittest.TestCase):
    def test_1_is_always_happy(self):
        self.assertEquals(True, HappyNumbers.is_happy_quick(1, list()))

    def test_2_3_4_5_6_8_9_are_not_happy(self):
        """
        2,3,4,5,6,8,9 are all unhappy numbers
        """
        numbers = [2,3,4,5,6,8,9]
        for num in numbers:
            self.assertEquals(False, HappyNumbers.is_happy_quick(num, list()))

    def test_7_is_happy(self):
        self.assertEquals(True, HappyNumbers.is_happy(7, list()))

    def test_powers_of_10_are_happy(self):
        """
        all powers of 10 are happy
        """
        for power in range(1,10):
            number = pow(10,power)
            self.assertEquals(True, HappyNumbers.is_happy_quick(number, list()))

    def test_check_random_numbers(self):
        for i in range(1,10):
            number = random.randint(1,100)
            self.assertEquals(HappyNumbers.is_happy(number,list()), HappyNumbers.is_happy_quick(number, list()))

if __name__=='__main__':
    unittest.main()
