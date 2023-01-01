from unittest import TestCase

from ..services import calc


class CalcTestCase(TestCase):
    def test_minus(self):
        res = calc(2, 2, '-')
        self.assertEqual(res, 0)

    def test_plus(self):
        res = calc(2, 2, '+')
        self.assertEqual(res, 4)

    def test_multiply(self):
        res = calc(2, 2, '*')
        self.assertEqual(res, 4)

    def test_div(self):
        res = calc(2, 2, '/')
        self.assertEqual(res, 1)
