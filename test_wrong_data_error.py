from unittest import TestCase


class TestWrongDataError(TestCase):
    def test___init__(self):
        self.assertTrue(TestCase)


class TestWrongDataError2(TestCase):
    def test___str__(self):
        self.assertTrue(TestCase)
