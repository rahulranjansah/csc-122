# """
#    *
#    * Sorting
#    *
#    * @author Rahul Ranjan Sah & Samriddha
#    * @date   03/19/2025
# """

from typing import TypeVar
T = TypeVar("T")


def max_selection_sort(lst: list[T]) -> None:
    n = len(lst)
    for i in range(n - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[i], lst[max_index] = lst[max_index], lst[i]



def sinking_sort(lst: list[T]) -> None:
    n = len(lst)
    for i in range(n):
        for j in range(n-1, i , -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
