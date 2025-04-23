"""Test code for zoo parser functionality."""

import os
from pathlib import Path

import unittest
from src.utilities import parse_utilities

class TestParseUtilities(unittest.TestCase):

    def run_parser_test(self, file_name : str, expected : list[str]) -> None:
        the_path = Path(os.path.abspath(file_name))

        with open(the_path, encoding="utf-8") as inf:
            contents = inf.readlines()

        filtered = parse_utilities.extract_valid_lines(contents)

        self.assertEqual(len(expected), len(filtered))

        for exp, filt_line in zip(expected, filtered):
            self.assertEqual(exp, filt_line)

    def test_parser(self):
        self.run_parser_test("data/zoo/zoo_empty.txt", [])
        self.run_parser_test("data/zoo/zoo_basic.txt", ["Adam tiger", "Phylis tiger", "George gorilla"])
        self.run_parser_test("data/zoo/zoo_all_animals.txt", \
                             ["Lola Tiger", "Chiffon		lion", "Razor			Mackerel", "Steven     gorilla"])