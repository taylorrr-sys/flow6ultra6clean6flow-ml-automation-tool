import unittest
from src.automation import Automator

class TestAutomation(unittest.TestCase):
    def test_automator_creation(self):
        automator = Automator()
        self.assertIsNotNone(automator.driver)