# """
#    *
#    * Weighted Die Class
#    *
#    * @author Rahul Ranjan Sah
#    * @date   02/06/2025
# """


from src.utilities.utility import conforms_to_a_die, is_monotonically_increasing, has_negative_values
import random

class WeightException(Exception):
    pass

class WeightedDie:

    def __init__(self, weights: list[int]):
        """
        Constructor method initializing instance variables and methods
        """
        # private method for invalid weights
        if not self.__weight_conform(weights):
            # weights = [1,1]
            raise WeightException("Invalid Input")

        # instance variables
        self._partial_sums = self.__partial_sums(weights)
        self._face_value = 0
        self.roll() # updates _face_value

        if not self.__partial_sums_conform():
            print(f"Partial sums with weights {weights} do not conform: {self._partial_sums}")
            print("Invalid die.")

    # private instance methods to call use it in constructors or public method
    def __weight_conform(self, weights: list[int]) -> bool:
        """ Private Instance method to check input weights
        """
        if has_negative_values(weights) or len(weights) <= 1:
            return False

        return True

    def __partial_sums(self, weights: list[int]) -> dict[int, int]:
        """Private instance method to compute partial sums for the given weights
        """
        partial_sums_dict = {}
        cumul_weight = 0

        # adding cumulative sum to each die roll
        for index, i in enumerate(range(1, len(weights)+1)):

            cumul_weight += weights[index]
            partial_sums_dict[i] = partial_sums_dict.get(i, 0) + cumul_weight

        return partial_sums_dict

    def __partial_sums_conform(self) -> bool:
        """Check if weights conform with utility functions
        """
        die_face_val_list = []
        die_partial_sum_list = []

        #  computing lists of keys and values of the dict to check for utility functions
        for key, value in self._partial_sums.items():
            die_face_val_list.append(key)
            die_partial_sum_list.append(value)

        if conforms_to_a_die(die_face_val_list) and is_monotonically_increasing(die_partial_sum_list):
            return True

        return False

    # public methods
    def get_face_value(self) -> int:
        """Public getter method for the face value
        """
        return self._face_value


    def roll(self) -> int:
        """Public roll method to generate face value based on the given weights
        """
        roller_val = random.randint(1, max(self._partial_sums.values()))

        # finding the relevant key and return
        for key,weight_value in self._partial_sums.items():
            if roller_val <= weight_value:
                self._face_value = key
                return self._face_value
