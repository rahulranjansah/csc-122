"""Test code for the weighted die rolling functionality."""

import unittest

from src.utilities.utility import has_negative_values, conforms_to_a_die, is_monotonically_increasing
from src.utilities.weighted_die import *

class TestWeightedDieRoller(unittest.TestCase):

    def run_die_rolls(self, die : WeightedDie, weights : list[int], expected_probs : list[float]):
        """
        simulating a number of rolls and comparing observed frequencies
        """
        die = WeightedDie(weights)

        results = [0] * (len(weights) + 1)
        NUM_ROLLS = 1000000
        for _ in range(NUM_ROLLS):
            results[die.roll()] += 1

        del results[0]

        for expected, computed in zip(expected_probs, results):
            self.assertAlmostEqual(expected, computed / NUM_ROLLS, places = 2) # Very loose bounds

    def compute_probs_then_run_rolls(self, die : WeightedDie, weights : list[int]):

        """
        comparing observed probabilties to check if they match
        """
        s = sum(weights)
        expected = [w / s for w in weights]

        # Run the test
        self.run_die_rolls(die, weights, expected)


    def test_roll(self):

        """
        Assertions for the testing of die rolls
        """

        # Fair 6-sided die test
        weights = [1, 1, 1, 1, 1, 1]
        fair = WeightedDie(weights)
        self.compute_probs_then_run_rolls(fair, weights)

        # 7-sided
        weights = [1, 0, 2, 4, 1, 1, 2]
        seven_sided = WeightedDie(weights)
        self.compute_probs_then_run_rolls(seven_sided, weights)

        # 8-sided
        weights = [1, 6, 2, 4, 1, 0, 2, 4]
        seven_sided = WeightedDie(weights)
        self.compute_probs_then_run_rolls(seven_sided, weights)


        # 9-sided
        weights = [1, 5, 2, 4, 2, 9, 2, 1, 6]
        seven_sided = WeightedDie(weights)
        self.compute_probs_then_run_rolls(seven_sided, weights)

        # 2-sided
        weights = [1, 0]
        two_sided = WeightedDie(weights)
        self.compute_probs_then_run_rolls(two_sided, weights)

        # bad weight input to a coin, defaults to [1,1]
        weights = [1, -1, 4, 2, 5]
        # die = WeightedDie(weights)
        # self.compute_probs_then_run_rolls(die, [1,1])

        self.assertRaises(WeightException, WeightedDie, weights)

        # bad input weight single value
        weights = [-1]
        # die = WeightedDie(weights)
        # self.compute_probs_then_run_rolls(die, [1,1])

        self.assertRaises(WeightException, WeightedDie, weights)

if __name__ == '__main__':
    unittest.main()