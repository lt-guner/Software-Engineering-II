import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):

    # test valid master card that ends in 0
    def test22(self):
        self.assertEqual(credit_card_validator("5372072285238760"), True)

    # test a valid master card but make it invalid with a 0 prefix and see if the function removes it
    def test23(self):
        self.assertEqual(credit_card_validator("05372079970727817"), False)

    # test if a valid master card with an appended 0 counts as valid card because of the 0 nullifier
    def test24(self):
        self.assertEqual(credit_card_validator("53720785725588020"), False)

    # test for test visa
    def test25(self):
        self.assertEqual(credit_card_validator("4111111111111111"), False)

    # test a valid card in reverse which has a correct prefix when reversed
    def test26(self):
        self.assertEqual(credit_card_validator("5467173615274755"), False)

    # test out of bounds prefix with a mastercard of 55 to 56 and still has valid checksum
    def test27(self):
        self.assertEqual(credit_card_validator("5674232370426481"), False)

    # passing an int
    def test28(self):
        self.assertEqual(credit_card_validator(4065972557141631), False)

    # upper boundary mastercard past 2720
    def test29(self):
        self.assertEqual(credit_card_validator("2721757189621781"), False)

    # lower boundary mastercard below 22221
    def test30(self):
        self.assertEqual(credit_card_validator("2220236045052404"), False)

    # reverse luhn on a visa
    def test31(self):
        self.assertEqual(credit_card_validator("4049849616444336"), False)

    # reverse luhn on mastercard
    def test32(self):
        self.assertEqual(credit_card_validator("5574236126766841"), False)

    # random luhn 16 digit
    def test33(self):
        self.assertEqual(credit_card_validator("9019797197600837"), False)

    # random luhn 15 digit
    def test34(self):
        self.assertEqual(credit_card_validator("623674792577990"), False)

    # passing as a list
    def test35(self):
        self.assertEqual(credit_card_validator([2254566705527611]), False)

    # pass a new line
    def test36(self):
        self.assertEqual(credit_card_validator("5372073954874240\n"), False)

    # test with trailing space
    def test37(self):
        self.assertEqual(credit_card_validator("5244072188255636 "), False)

    # test with pre space
    def test38(self):
        self.assertEqual(credit_card_validator(" 5244072188255636"), False)

    # f string
    def test39(self):
        validcard = "5326137043953518"
        self.assertEqual(credit_card_validator(f'{validcard}'), True)

    # declare an int to a string
    def test40(self):
        self.assertEqual(credit_card_validator(str(5196659675123026)), True)

    # test newline as input
    def test41(self):
        self.assertEqual(credit_card_validator("\n"), False)