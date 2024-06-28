from django.test import SimpleTestCase
from app import calc


class Test(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(10, 5)
        self.assertEqual(res, 15)

    def test_subtract_numbers(self):
        res = calc.subtract(20, 5)
        self.assertEqual(res, 15)
