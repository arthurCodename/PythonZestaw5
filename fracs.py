import unittest


def add_frac(frac1, frac2):
    if frac1[1] == frac2[1]:
        fraction = frac1[0] + frac2[0]
        return [fraction, frac1[1]]
    else:
        fraction = (frac1[0] * frac2[1]) + (frac2[0] * frac1[1])
        return [fraction, frac1[1] * frac2[1]]


def sub_frac(frac1, frac2):
    if frac1[1] == frac2[1]:
        fraction = frac1[0] - frac2[0]
        return [fraction, frac1[1]]
    else:
        fraction = (frac1[0] * frac2[1]) - (frac1[1] * frac2[0])
        return [fraction, (frac1[1] * frac2[1])]


def mul_frac(frac1, frac2):
    return [(frac1[0] * frac2[0]), (frac1[1] * frac2[1])]


def div_frac(frac1, frac2):
    return [frac1[0] * frac2[1], frac1[1] * frac2[0]]


def is_positive(frac):
    return frac[0] / frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    if frac1[0] / frac1[1] > frac2[0] / frac2[1]:
        return 1
    elif frac1[0] / frac1[1] == frac2[0] / frac2[1]:
        return 0
    else:
        return -1


def frac2float(frac):
    return float(frac[0] / frac[1])


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 4], [2, 4]), [4, 4])


    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 4], [1, 2]), [2, 8])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 4], [1, 2]), [3, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac([3, 4], [1, 2]), [6, 4])

    def test_is_positive(self):
        self.assertEqual(is_positive([-2, -4]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 4]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)

    def frac2float(self):
        self.assertEqual(frac2float([1, 5]), 0.2)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
