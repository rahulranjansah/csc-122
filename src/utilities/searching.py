# """
#    *
#    * Searching
#    *
#    * @author Rahul Ranjan Sah & Samriddha
#    * @date   03/18/2025
# """

# local imports
from typing import TypeVar
T = TypeVar("T")

def ensure_order(idx1 : int, idx2 : int) -> int:
    """Return (min, max) of the given values"""
    return (idx1, idx2) if idx1 < idx2 else (idx2, idx1)

def norm_index(index: int, size : int) -> int:
    """Force an index to be positive"""
    return index if index >= 0 else index + size

def normalize(start_index : int, end_index : int, sz : int) -> tuple[int, int]:
    """Force indices to be positive and in the proper order"""
    return ensure_order(norm_index(start_index, sz), norm_index(end_index, sz))

def binary_search(data: list[T], target: T, start_idx : int = 0, end_idx : int = -1) -> int:

    """Runs standard binary search and returns invalid index when nothing is found"""

    left_idx, right_idx = normalize(start_idx, end_idx, len(data))

    while left_idx <= right_idx:

        middle_idx = (left_idx + right_idx) // 2

        # Target is less than the middle element
        if target < data[middle_idx]:
            right_idx = middle_idx - 1

        # Target greater than the middle element
        elif data[middle_idx] < target:
            left_idx = middle_idx + 1

        # Found it
        else:
            return middle_idx

    return -len(data) - 1

def trinary_search(data: list[T], target: T, start_idx : int = 0, end_idx : int = -1) -> int:

    """Runs trinary search and returns invalid index when nothing is found"""

    left_idx, right_idx = normalize(start_idx, end_idx, len(data))

    while left_idx <= right_idx:

        portion = (right_idx - left_idx) // 3
        middle1 = left_idx + portion
        middle2 = right_idx - portion

        # target at middle1
        if target == data[middle1]:
            return middle1

        # target at middle2
        if target == data[middle2]:
            return middle2

        # target smaller than middle1 index
        if target < data[middle1]:
            right_idx = middle1 - 1

        # target greater than middle2 index
        elif target > data[middle2]:
            left_idx = middle2 + 1

        else:
            left_idx = middle1 + 1
            right_idx = middle2 - 1

    return -len(data) - 1



def binary_search_valid_index(data: list[T], target: T, start_idx : int = 0, end_idx : int = -1) -> int:
    """Perform binary search, but instead of returning a failure when target is not found, we
       return the index where the target should have been"""

    left_idx, right_idx = normalize(start_idx, end_idx, len(data))

    while left_idx <= right_idx:

        middle_idx = (left_idx + right_idx) // 2

        # Target is less than the middle element
        if target < data[middle_idx]:
            right_idx = middle_idx - 1

        # Target greater than the middle element
        elif data[middle_idx] < target:
            left_idx = middle_idx + 1

        # Found it
        else:
            return middle_idx

    return left_idx

def trinary_search_valid_index(data: list[T], target: T, start_idx : int = 0, end_idx : int = -1) -> int:
    """Perform trinary search, but instead of returning a failure when target is not found, we
       return the index where the target should have been"""

    left_idx, right_idx = normalize(start_idx, end_idx, len(data))

    while left_idx <= right_idx:

        portion = (right_idx - left_idx) // 3
        middle1 = left_idx + portion
        middle2 = right_idx - portion

        if target == data[middle1]:
            return middle1

        if target == data[middle2]:
            return middle2

        if target < data[middle1]:
            right_idx = middle1 - 1

        elif target > data[middle2]:
            left_idx = middle2 + 1

        else:
            left_idx = middle1 + 1
            right_idx = middle2 - 1

    return left_idx


