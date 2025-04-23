# """Test code for the weighted die rolling functionality."""

# import unittest
# from src.utilities.weighted_die_roller import roll, partial_sums
# # from src.utilities.utility_functions import conforms_to_a_die, is_monotonically_increasing, has_negative_values

# class TestWeightedDieRoller(unittest.TestCase):

#     def run_die_rolls(self, weights : list[int], expected_probs : list[float]):
#         results = [0] * (len(weights) + 1)
#         NUM_ROLLS = 1000000
#         for _ in range(NUM_ROLLS):
#             results[roll(weights)] += 1

#         del results[0]

#         for expected, computed in zip(expected_probs, results):
#             self.assertAlmostEqual(expected, computed / NUM_ROLLS, places = 2) # Very loose bounds

#     def compute_probs_then_run_rolls(self, weights : list[int]):

#         # Compute expected probabilities
#         s = sum(weights)
#         expected = [w / s for w in weights]

#         # Run the test
#         self.run_die_rolls(weights, expected)

#     def test_roll(self):

#         # Fair 6-sided die test
#         self.compute_probs_then_run_rolls([1, 1, 1, 1, 1, 1])

#         # 7-sided
#         self.compute_probs_then_run_rolls([1, 2, 4, 1, 1, 2])

#         # other tests
#         self.compute_probs_then_run_rolls([1, 0, 1, 2, 1, 1, 7, 9])
#         self.compute_probs_then_run_rolls([1, 0, 1, 2, 1, 1, 7, 9, 0])
#         self.compute_probs_then_run_rolls([1, 0, 2, 1, 1, 7, 9])

# if __name__ == '__main__':
#     unittest.main()