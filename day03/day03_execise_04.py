import unittest


class TestDemo1(unittest.TestCase):
    def setUp(self):
        print("--- setUp ---")
    def tearDown(self):
        print("--- setDown")
    def test_b(self):
        print("test_b")

    def test_a(self):
        print("test_a")

    def testA(self):
        print("test_A")


class TestDemo2(unittest.TestCase):
    def test_b(self):
        print("test_b")

    def test_a(self):
        print("test_a")

    def testA(self):
        print("test_A")
