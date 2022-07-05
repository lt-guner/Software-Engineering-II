# Class: CS362
# Term: Winter 2022
# Homework: HW3: Random Testing
# Author: Timur Guner

from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):

    def testcard(self):

        # generate a lot of numbers
        for x in range(1000000):

            # generate a random number between length 14 and 17
            card_number = random.randint(10000000000000, 99999999999999999)

            # change it to a string
            card_number_string = str(card_number)

            # pass it to the card validator
            credit_card_validator(card_number_string)


if __name__ == '__main__':
    unittest.main()
