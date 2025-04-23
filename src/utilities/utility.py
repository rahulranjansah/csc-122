# """Utility functions robust implementation of the die roller code
# """
# checks if the weight_list has negative val
def has_negative_values(arr: list[int]) -> bool:

    """Checks if weighted values list has any negative number
    """
    for val in arr:
        if val < 0:
            return True

    return False

# checks if weights in a list confirms to a die
def conforms_to_a_die(arr: list[int]) -> bool:
    """Confirms it is a n-numbered finite die
    """
    arr.sort()
    for index, face_val in enumerate(arr, start=1):
        if index != face_val:
            return False
    return True

# # cumulative sum is always increasing for the weighted list
def is_monotonically_increasing(arr: list[int]) -> bool:
    """Confirms Monotonically increasing cumulative sum for the function
    """
    cum_sum = 0
    itr_sum = 0

    for val in arr:
        itr_sum += val

        if itr_sum >= cum_sum:
            cum_sum = itr_sum
        else:
            return False

    return True

