import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):

    # checks 0 as input
    def test00(self):
        self.assertEqual(credit_card_validator("0"), False)
        pass

    # checks for empty input
    def test01(self):
        self.assertEqual(credit_card_validator(""), False)
        pass

    # some visa checks ----------------------------------------------------------------------------------------------

    # check valid visa with correct check number and length
    def test02(self):
        self.assertEqual(credit_card_validator("4065972557141631"), True)

    # check valid visa with wrong check number and length correct length
    def test03(self):
        self.assertEqual(credit_card_validator("4547506716347159"), False)

    # check visa with valid check number and wrong length
    def test04(self):
        self.assertEqual(credit_card_validator("404984963232324"), False)

    # check visa with wrong check number and wrong length
    def test05(self):
        self.assertEqual(credit_card_validator("406570070213605"), False)

    # test American Express 34 -------------------------------------------------------------------------------------

    # valid amex 34 card with correct check num and length
    def test06(self):
        self.assertEqual(credit_card_validator("349610255634178"), True)
        pass

    # valid length amex34 but wrong but wrong check num
    def test07(self):
        self.assertEqual(credit_card_validator("349621342510323"), False)

    # valid amex34 check sum correct but wrong length
    def test08(self):
        self.assertEqual(credit_card_validator("3496765536430096"), False)

    # amex34 with wrong length and checksum
    def test09(self):
        self.assertEqual(credit_card_validator("3493808644143687"), False)

    # test American Express 37 -------------------------------------------------------------------------------------

    # valid 37 prefix amex
    def test10(self):
        self.assertEqual(credit_card_validator("370008525273103"), True)
        pass

    # valid 37 length but incorrect checksum
    def test11(self):
        self.assertEqual(credit_card_validator("370008100251888"), False)
        pass

    # amex 37 with valid check sum but wrong length
    def test12(self):
        self.assertEqual(credit_card_validator("3700246006077314"), False)
        pass

    # amex 37 with wrong length and check sum
    def test13(self):
        self.assertEqual(credit_card_validator("3700365454155526"), False)

    # test MasterCard 51-55 -----------------------------------------------------------------------------------------

    # test valid mastercard
    def test14(self):
        self.assertEqual(credit_card_validator("5574236968584180"), True)

    # test mastercard with correct length but wrong check code
    def test15(self):
        self.assertEqual(credit_card_validator("5372070522215678"), False)

    # test that has correct check but wrong length
    def test16(self):
        self.assertEqual(credit_card_validator("55742317376271498"), False)

    # wrong length and check number
    def test17(self):
        self.assertEqual(credit_card_validator("53720734276128882"), False)

    # test mastercard 2221-2720 --------------------------------------------------------------------------------------

    # test valid master card
    def test18(self):
        self.assertEqual(credit_card_validator("2254566705527611"), True)

    def test19(self):
        self.assertEqual(credit_card_validator("2720123456781231"), True)

    # test correct length but wrong check sum
    def test20(self):
        self.assertEqual(credit_card_validator("2720115611687494"), False)

    # test wrong length but correct check sum
    def test21(self):
        self.assertEqual(credit_card_validator("22277336181430135"), False)

    # check wrong length and check sum
    def test22(self):
        self.assertEqual(credit_card_validator("27079798727055929"), False)

    # testing out of bounds -----------------------------------------------------------------------------------------

    # test out of bounds prefix with a mastercard of 55 to 56 and still has valid checksum
    def test23(self):
        self.assertEqual(credit_card_validator("5612568741354562"), False)

    # test out of bounds prefix with a mastercard of 51 to 50 and still has valid checksum
    def test24(self):
        self.assertEqual(credit_card_validator("5012568741354568"), False)

    # upper boundary mastercard past 2720 but with valid length and checksum
    def test25(self):
        self.assertEqual(credit_card_validator("2722124567815452"), False)

    # lower boundary mastercard below 22221 but with valid length and checksum
    def test26(self):
        self.assertEqual(credit_card_validator("2220121258587413"), False)

    # test lower boundary of Amex <33 but with valid length and checksum
    def test27(self):
        self.assertEqual(credit_card_validator("339357513747118"), False)

    # test between 33 and 37 for Amex but with valid length and checksum
    def test28(self):
        self.assertEqual(credit_card_validator("359357513747116"), False)

    # test above 37 for amex with correct length and checksum
    def test29(self):
        self.assertEqual(credit_card_validator("380036185765570"), False)

    # check visa with prefix of 3 but correct length and checksum
    def test30(self):
        self.assertEqual(credit_card_validator("3020374683880149"), False)

    # check visa with prefix bfo 5 but correct length and checksum
    def test31(self):
        self.assertEqual(credit_card_validator("5020374683880144"), False)

    # some other credit cards with non Amex, MC, or Visa prefix ----------------------------------------------------

    # test a Discover card
    def test81(self):
        self.assertEqual(credit_card_validator("6011302474173238"), False)

    # test JCB
    def test82(self):
        self.assertEqual(credit_card_validator("3556915616813185"), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
