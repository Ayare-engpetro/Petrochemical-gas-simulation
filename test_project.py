
import unittest
from main import calculate_pressures

class TestGasSimulation(unittest.TestCase):
    def test_simulation_exists(self):
        # Test if the core calculation function is defined properly
        self.assertTrue(callable(calculate_pressures))

if __name__ == "__main__":
    unittest.main()
