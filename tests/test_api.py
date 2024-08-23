import unittest
from src.api import get_stratifications

class TestApi(unittest.TestCase):

    def test_get_stratifications(self):
        result = get_stratifications()
        self.assertIsInstance(result, dict)  # Example test case

if __name__ == "__main__":
    unittest.main()
