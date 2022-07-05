import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    # test val > 100 and < 150 for true
    def test1(self):
        val = 101
        self.assertEqual(contrived_func(val), True)

    # test (val * 5 < 361 and val / 2 < 24) and val == 6 with both (val * 5 < 361 and val / 2) being true
    def test2(self):
        val = 6
        self.assertEqual(contrived_func(val), False)

    # test (val * 5 < 361 and val / 2 < 24) and val != 6 with both (val * 5 < 361 and val / 2) being true
    def test3(self):
        val = 2
        self.assertEqual(contrived_func(val), True)

    # all others ifs do not succeed meaning the last else is executed
    def test4(self):
        val = 1001
        self.assertEqual(contrived_func(val), False)

    # testing the out of bounds for val > 100 and < 150 but valid test for (val > 75 or val / 8 < 10) and
    # val**val % 5 == 0 with 100 for val > 75 bein true
    def test5(self):
        val = 100
        self.assertEqual(contrived_func(val), True)

    # valid test to for (val > 75 or val / 8 < 10) and val**val % 5 == 0 where val / 80 is true
    def test6(self):
        val = 60
        self.assertEqual(contrived_func(val), True)

    # test (val * 5 < 361 and val / 2 < 24) and val == 48 which val * 5 < 361 is true and val / 2 < 24 is false
    def test7(self):
        val = 48
        self.assertEqual(contrived_func(val), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
