# """
#    *
#    * Id factory Class
#    *
#    * @author Rahul & Samriddha
#    * @date   02/19/2025
# """


from src.zoo.animals import *

class Zoo():
    def __init__(self) -> None:

        """Initializing constructor
        """
        self._animals = {}

    def add_animal(self, name: str, animal: Animal) -> bool:

        """Adds animal in the dictonary and returns if they added"""

        if name in self._animals:
            return False
        else:
            self._animals[name] = animal
            return True

    def remove_animal(self, name: str) -> bool:

        """Bool val of removing animal and checking
        """

        if name in self._animals:
            del self._animals[name]
            return True

        return False

    def get_animal(self, name: str) -> Animal:

        """Get animal name from the animal dictionary
        """

        if name in self._animals:
            return self._animals.get(name)
        else:
            raise KeyError(f"Unknown Key {name}")

    def status(self, name: str) -> AnimalStatus:

        """Returns animal status
        """

        return self._animals[name].status()

    def update(self) -> list[tuple[str, Animal]]:

        """Updates the list of perished animals
        """

        perished = []
        for name, animal in list(self._animals.items()):
            alive = animal.update()
            if not alive:
                perished.append((name, animal))
                del self._animals[name]

        return perished


    def __contains__(self, name: str) -> bool:

        """Checks if a name is in the dictionary
        """

        if name in self._animals:
            return True

        return False

    def __len__(self) -> int:
        """Measures the length of the dictionary
        """

        return len(self._animals)


