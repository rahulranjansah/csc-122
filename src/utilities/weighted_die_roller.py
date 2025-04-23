
# from src.utilities.utility import conforms_to_a_die, is_monotonically_increasing, has_negative_values
# import random

# def partial_sums(weights : list[int]) -> dict[int, int]:
#     """
#     Computes and returns a dictionary of partial sums from a given list of values.
#     Recall, a partial sum refers to the sum of all prior values in the list. For
#     example, with list [3, 2, 1, 6, 4, 1]:
#          Input List    (Calculation)    Partial Sums Dictionary
#               3            0 + 3               1 : 3
#               2            3 + 2               2 : 5
#               1            5 + 1               3 : 6
#               6            6 + 6               4 : 12
#               4           12 + 4               5 : 16
#               1           16 + 1               6 : 17
#     """
#     partial_sums_dict = {}
#     cumul_weight = 0

#     # adding cumulative sum to each die roll
#     for index, i in enumerate(range(1, len(weights)+1)):
#         cumul_weight += weights[index]
#         partial_sums_dict[i] = partial_sums_dict.get(i, 0) + cumul_weight

#     return partial_sums_dict


# def roll(weights : list[int]) -> int:

#     """Initiate rolling by checking input / output then actually performing a dice roll"""
#     if has_negative_values(weights):
#         return -1

#     # calling partial sum mapping
#     partial_sum_dict = partial_sums(weights)

#     # validate sides conform to die and value of the partial sum dict.

#     # random val generation
#     roller_val = random.randint(1, max(partial_sum_dict.values()))

#     # list comprehension of mapped value
#     roller_val_list = [val for val in partial_sum_dict.values()]
#     roller_key_list = [key for key in partial_sum_dict.keys()]

#     if not is_monotonically_increasing(roller_val_list) or not conforms_to_a_die(roller_key_list):
#         return -1

#     # accessing key-value pair
#     for index, val in enumerate(roller_val_list):

#         if roller_val <= val:
#             if index == 0:
#                 index_val = index

#             index_val = index
#             break

#     for key, value in partial_sum_dict.items():
#         if roller_val_list[index_val] == value:
#             return key


# weights = [3,2,1,6,4,1,6,7,8]
# print(f"Weight Die Rolls: {roll(weights)}")