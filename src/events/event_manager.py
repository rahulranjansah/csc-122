from abc import ABC, abstractmethod
from src.zoo.animals import Animal
from collections.abc import Callable
from src.events.events import Event
from src.utilities.containers.doubly_linked_list import DNode, DoublyLinkedList

class EventManager():

    def __init__(self) -> None:
        dll = DoublyLinkedList()
        self._eventlist = dll

    def register(self, event: 'Event') -> None:

        """
        Adds an event to the manager and maintains sorted ordering
        based on start time.
        """

        # inserting as input
        self._eventlist.push_back(event)


    def __indices_of_event_with(self, animal: Animal) -> list[Event]:

        """
        Returns the indices of all events associated with the given animal.
        """

        indices = []

        for i, event in enumerate(self._eventlist):
            if event.get_animal() == animal:
                indices.append(i)

        return indices

    def events_with(self, animal: Animal) -> list[Event]:
        """
        Returns all events associated with the given animal.
        """
        events = []

        for event in self._eventlist:
            if event.get_animal() == animal:
                events.append(event)

        return events

    def remove_all(self, animal: Animal) -> int:
        """
        Removes all events that referred to the given animal.
        """
        indices = self.__indices_of_event_with(animal)

        for index in indices:
            self._eventlist.pop(index)

        return len(indices)

    def events_start_before(self, ticks: int) -> list[Event]:
        """
        Returns all events that start before (<) the given time.
        """
        before = []

        for event in self._eventlist:
            if event._start_time < ticks:
                before.append(event)

        return before


    def events_start_now_and_later(self, ticks: int) -> list[Event]:

        """
        Returns all events that start before (>=) the given time.
        """
        after = []

        for event in self._eventlist:
            if event._start_time >= ticks:
                after.append(event)

        return after

    def __len__(self) -> int:
        """Returns the number of event being managed"""

        return len(self._eventlist)



