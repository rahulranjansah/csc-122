"""Test code for the zoo file parser functionality."""

import unittest
import tempfile
import os
from src.zoo.zoo import Zoo
from src.input.zoo_file_parser import ZooFileParser, ZooParseException

class TestZooFileParser(unittest.TestCase):

    def setUp(self):
        """Create temporary test files for different cases"""
        self.test_dir = tempfile.TemporaryDirectory()
        self.valid_zoo_file = os.path.join(self.test_dir.name, "valid_zoo.txt")
        self.invalid_format_file = os.path.join(self.test_dir.name, "invalid_format.txt")
        self.unknown_animal_file = os.path.join(self.test_dir.name, "unknown_animal.txt")

        # Valid zoo file
        with open(self.valid_zoo_file, "w") as f:
            f.write("Adam tiger\nPhylis tiger\nGeorge gorilla\n")

        # Invalid format (missing animal type)
        with open(self.invalid_format_file, "w") as f:
            f.write("Adam\n")

        # Unknown animal type
        with open(self.unknown_animal_file, "w") as f:
            f.write("Xander dragon\n")

    # def test_valid_zoo_file(self):
    #     """Test that a valid zoo file is parsed correctly"""
    #     parser = ZooFileParser(self.valid_zoo_file)
    #     zoo = parser.get_zoo()
    #     self.assertIsInstance(zoo, Zoo)
    #     self.assertEqual(len(zoo), 3)
    #     self.assertIn("Adam", zoo.get_animal)
    #     self.assertIn("Phylis", zoo.get_animal)
    #     self.assertIn("George", zoo.get_animal)

    def test_invalid_format(self):
        """Test that a file with incorrect format raises an exception"""
        with self.assertRaises(ZooParseException):
            ZooFileParser(self.invalid_format_file)

    def test_unknown_animal(self):
        """Test that an unknown animal type raises an exception"""
        with self.assertRaises(ZooParseException):
            ZooFileParser(self.unknown_animal_file)

if __name__ == "__main__":
    unittest.main()

