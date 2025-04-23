# """
#    *
#    * Id factory Class
#    *
#    * @author Rahul Ranjan Sah
#    * @date   03/12/2025
# """

"""A zoo file defines the contents of a zoo:
      * animals
      * etc....TBD
"""
import os
from pathlib import Path

import src.utilities.parse_utilities as parse_utilities

from src.zoo.zoo import Zoo
import src.zoo.animals as animals

class ZooParseException(Exception):
    pass

class ZooFileParser():
    """Parse files of the form:

        # A zoo file consists of parts:
        #   (1) Animals
        #   (2) Etc.
        #
        #
        # Animals are of the form:
        #
        #     <unique-id> <type>
        #
        Adam tiger     # Adam is the name of a tiger
        Phylis tiger   # Phylis is also a tiger
        George gorilla
    """

    def __init__(self, zoo_file : str) -> None:
        """Automatically initiates the parse

        @input: zoo file path

        @implicit output: populates a Zoo object
        """
        self._zoo_path = Path(os.path.abspath(zoo_file))

        if not self._zoo_path.is_file():
            raise ZooParseException(f"File {zoo_file} not found: {self._zoo_path}.")

        self._zoo = Zoo()

        if not self._do_parse():
            raise ZooParseException(f"Parsing of zoo file {zoo_file} failed.")

    #
    # Accessors
    #
    def get_zoo(self):
        """Returns the zoo objecr built during parsing"""
        return self._zoo

    #
    # Parsing
    #
    def _do_parse(self) -> bool:
        """
        Start of actual parsing of the playback file:
           (1) Remove comments      <- parse utilities method
           (2) Process the lines:   <- _extract
               (a) animals
               (b) ...
        """
        print(f"Attempting to  parse zoo file {self._zoo_path}.")

        with open(self._zoo_path, encoding="utf-8") as inf:
            contents = inf.readlines()

        # Read line by line, ignore comments
        # Result is a list of lines (strings with text)
        filtered = parse_utilities.extract_valid_lines(contents)

        if len(filtered) <= 0:
            print(f"Zoo file {self._zoo_path} is empty")
            return True

        # Builds the sequence of events
        return self._extract(filtered)

    def _extract(self, lines: [str]) -> bool:
        """Extract all animals
        @input: lines -- contents of the input file as a list of strings
        @output: return True if parsing for the entire file was successful;
                 returns False when there are any parsing errors.
        @exceptions: Observe that __init__ raises an exception if parsing
                     fails so this method DOES NOT raise an exception directly.
        @implicit output: populates a Zoo object for valid input
        """

        for line in lines:
            line = line.split("#")[0].strip()

            if line:
                parts = line.split()
                if len(parts) != 2:
                    print(f"Invalid line format: {line}")
                    return False

                unique_id, animal_type = parts
                animal_obj = self.str_to_animal_obj(animal_type)
                self._zoo.add_animal(unique_id, animal_obj)

        return True


    @staticmethod
    def str_to_animal_obj(animal : str) -> animals.Animal:
        """Convert str(animal) -> Animal
            e.g., "Tiger" -> Tiger()
        """

        # Loop through all the animal classes and create a corresponding object of that type
        import sys, inspect
        for name, the_class in inspect.getmembers(animals):
            if inspect.isclass(the_class):

                # Facilitate case-insensitivty
                if name.lower() == animal.lower():
                    return the_class(start_energy=50, max_energy=100)

        raise ZooParseException(f"Animal type {animal} does not have a corresponding class definition")