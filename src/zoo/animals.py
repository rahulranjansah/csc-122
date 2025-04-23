# """
#    *
#    * Id factory Class
#    *
#    * @author Rahul Ranjan Sah
#    * @date   02/12/2025
# """

# local import
from src.utilities.id_factory import IdFactory

# global import
from enum import Enum
import math
from abc import ABC, abstractmethod

class AnimalException(Exception):
    pass

class AnimalStatus(Enum):

    """Class to generate enumeration for possible scenario values
    """

    NOT_ALIVE = 0
    WEAK = 1
    NORMAL = 2
    FULL = 3

class Animal(ABC):

    """Main class collecting animals status and update energy levels"""

    # single static copy
    __id_factory = IdFactory()
    WEAKNESS_THRESHOLD = 0.25
    NORMAL_THRESHOLD = 0.90

    # constructor initializing start and max energy
    def __init__(self, start_energy: int, max_energy:  int) -> None:

        """Constructor methods initializing instance variables"""

        # instance variables
        self._id = next(Animal.__id_factory)

        self._DEFAULT_MAX_ENERGY = 100
        self._DEFAULT_START_ENERGY_PERCENTAGE = 0.5
        self._MAX_ENERGY = max_energy

        # checks for start energy None
        if start_energy:

            if start_energy == 0:
                self._MAX_ENERGY = 0
                self._energy = 0

            # start energy equals to max energy
            elif abs(start_energy) == abs(max_energy):
                if max_energy < 0:
                    self._energy = -self._MAX_ENERGY * self._DEFAULT_START_ENERGY_PERCENTAGE
                else:
                    self._energy = max_energy

            # start energy greater than max energy
            elif abs(start_energy) > abs(max_energy):
                if max_energy < 0:
                    self._energy = - self._MAX_ENERGY * self._DEFAULT_START_ENERGY_PERCENTAGE
                else:
                    self._energy = (self._MAX_ENERGY * self._DEFAULT_START_ENERGY_PERCENTAGE)

            else:
                self._MAX_ENERGY = max_energy
                self._energy = start_energy

        else:
            self._energy = abs(self._MAX_ENERGY * self._DEFAULT_START_ENERGY_PERCENTAGE)

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def speak(self):
        pass


    def status(self) -> AnimalStatus:

        """Function status returning and using user defined datatype AnimalStatus and
        checking if aminal is alive, weak, normal, or dead
        """

        # enumerated checks
        if self._energy <= 0:
            return AnimalStatus.NOT_ALIVE

        elif self._energy <= Animal.WEAKNESS_THRESHOLD * self._MAX_ENERGY:
            return AnimalStatus.WEAK

        elif self._energy <= Animal.NORMAL_THRESHOLD * self._MAX_ENERGY:
            return AnimalStatus.NORMAL

        else:
            return AnimalStatus.FULL

    def update(self) -> bool:
        """Reduces energy by 1 and returns if the animal is still alive."""

        if self._energy <= 0:
            raise AnimalException(f"Animal {self._id} is dead")

        self._energy -= 1
        return self._energy > 0


# class Fish inheriting from Animal class
class Fish(Animal):

    def eat(self, amount: int) -> int:

        """changes and updates the value of energy based on possible defaults and values"""

        self._energy += amount
        self._energy = math.floor(min(self._energy, self._MAX_ENERGY))
        return self._energy

# class Mammal inheriting from Animal class
class Mammal(Animal):

    """Mammal class with instances inherited from main Animal class"""

    def eat(self, amount: int) -> int:

        """changes and updates the value of energy based on possible defaults and values"""

        self._energy += (amount * (1/2))
        self._energy = math.floor(min(self._energy, self._MAX_ENERGY))
        return self._energy

# layers of classes in between
class Cat(Mammal):
    pass

class Primate(Mammal):
    pass

class Mackerel(Fish):

    def speak(self) -> str:

        """Mackerel speaks"""
        return f"Mackerel {self._id} says blub"

class Lion(Cat):

    def speak(self) -> str:
        """Lion speaks"""
        return f"Lion {self._id} says roar"

class Tiger(Cat):

    def speak(self) -> str:
        """Tiger speaks"""
        return f"Tiger {self._id} says rawr"

class Gorilla(Primate):

    def speak(self) -> str:
        """Gorilla speaks"""
        return f"Gorilla {self._id} says grunt"


gorilla = Gorilla(start_energy=23, max_energy=40)
print(gorilla.status)