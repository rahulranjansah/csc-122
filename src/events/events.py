from abc import ABC, abstractmethod
from src.zoo.animals import Animal
from collections.abc import Callable

class EventException(Exception):
    pass

class Event(ABC):

    def __init__(self, start: int, animal: Animal, action: Callable, reps = 1, arg: int = None) -> None:

        """Constructor methods initializing instance variables"""

        self._start_time = start
        self._animal = animal
        self._action = action
        self._invocations = 0
        self._REPETITIONS = reps
        self.opt_amount_arg = arg

    def get_animal(self) -> Animal:
        return self._animal

    def invoke(self) -> None:

        if self._action:
            self._invocations += 1

        else:
            raise EventException(f"No action was performed")

    def __lt__(self, that: 'Event') -> bool:
        return self._start_time < that._start_time

    def __eq__(self, that: 'Event') -> bool:
        return self._start_time == that._start_time

    def __neq__(self, that: 'Event') -> bool:
        return self._start_time != that._start_time

    @abstractmethod
    def should_invoke(self, ticks: int) -> bool:
        pass

    def __str__(self):
        pass


class OneTimeEvent(Event):

    def __init__(self, start, animal, action, arg: int = None):

        super().__init__(start, animal, action, arg)

    def should_invoke(self, ticks: int) -> bool:
        return ticks == self._start_time and self._invocations < 1

    def __str__(self) -> str:
        return f"{self._start_time}, {self._animal}, {self._action}"

class RecurringEvent(Event):

    def __init__(self, start, animal, action, period, reps, arg: int = None):

        super().__init__(start, animal, action, reps, arg)
        self._period = period

    def should_invoke(self, ticks: int) -> bool:

        """Check if this recurring event should be invoked
        """

        if self._REPETITIONS >= 0 and self._invocations >= self._REPETITIONS and ticks < self._start_time:
            return False

        return (ticks - self._start_time) % self._period == 0


    def __str__(self) -> str:
        return f"{self._start_time}, {self._animal}, {self._action}"



