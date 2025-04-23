# """
#    *
#    * Id factory Class
#    *
#    * @author Rahul Ranjan Sah
#    * @date   02/12/2025
# """

# global imports
from enum import Enum

class IdFactory:

    """IdFactor generates id from index 0
    """

    # standard constructor
    def __init__(self) -> None:
        """Initializes the id factory and takes itself and returns one
        """
        self._current_id = 0

    # next special constructor
    def __next__(self) -> int:
        """
        Increases the current id counter by 1
        """

        # saves the initial value index 0
        current = self._current_id
        self._current_id += 1

        return current
