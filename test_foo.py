from unittest import TestCase


class TestMe(TestCase):
    def test_1(self):
        self.assertEqual(True, True)
    def test_2(self):
        self.assertEqual(True, False)
