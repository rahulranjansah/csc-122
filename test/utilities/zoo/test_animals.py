"""Test code for all animals."""

import unittest
from src.zoo.animals import *

class TestAnimals(unittest.TestCase):

    def test_animal_extreme_construction(self):

        max_energy = 1000

        a = Lion(0, max_energy)
        self.assertEqual(max_energy * a._DEFAULT_START_ENERGY_PERCENTAGE, a._energy)

        a = Lion(1, max_energy)
        self.assertEqual(1, a._energy)

        a = Lion(max_energy + 1, max_energy)
        self.assertEqual(max_energy * a._DEFAULT_START_ENERGY_PERCENTAGE, a._energy)

        a = Lion(max_energy, max_energy)
        self.assertEqual(max_energy, a._energy)

        max_energy = -1000

        a = Lion(0, max_energy)
        self.assertEqual(-max_energy * a._DEFAULT_START_ENERGY_PERCENTAGE, a._energy)

        a = Lion(1, max_energy)
        self.assertEqual(1, a._energy)

        a = Lion(-max_energy + 1, max_energy)
        self.assertEqual(-max_energy * a._DEFAULT_START_ENERGY_PERCENTAGE, a._energy)

        a = Lion(max_energy, max_energy)
        self.assertEqual(-max_energy * a._DEFAULT_START_ENERGY_PERCENTAGE, a._energy)

        max_energy = -500

        a = Mackerel(max_energy, max_energy)
        self.assertEqual(-max_energy * a._DEFAULT_START_ENERGY_PERCENTAGE, a._energy)

        max_energy = 120

        a = Tiger(1, max_energy)
        self.assertEqual(1, a._energy)

    def test_speak(self):
        """Checks for animal and with their id speaking
        """
        mackerel = Mackerel(start_energy=50, max_energy=100)
        tiger = Tiger(start_energy=50, max_energy=100)
        lion = Lion(start_energy=50, max_energy=100)
        gorilla = Gorilla(start_energy=0, max_energy=20)

        self.assertRegex(mackerel.speak(), r"Mackerel \d+ says blub")
        self.assertEqual(mackerel.speak(), f"Mackerel {mackerel._id} says blub")
        self.assertEqual(tiger.speak(), f"Tiger {tiger._id} says rawr")
        self.assertEqual(lion.speak(), f"Lion {lion._id} says roar")
        self.assertEqual(gorilla.speak(), f"Gorilla {gorilla._id} says grunt")

    def test_status(self):

        fish = Mackerel(start_energy=0, max_energy=100)

        fish._energy = 0
        self.assertEqual(fish.status(), AnimalStatus.NOT_ALIVE)

        # Test Weak status
        fish._energy = 10
        self.assertEqual(fish.status(), AnimalStatus.WEAK)
        fish._energy = 25
        self.assertEqual(fish.status(), AnimalStatus.WEAK)

        # Test NORMAL status (energy > 25 and <= 90)
        fish._energy = 50
        self.assertEqual(fish.status(), AnimalStatus.NORMAL)
        fish._energy = 90
        self.assertEqual(fish.status(), AnimalStatus.NORMAL)

        # Test FULL status (energy > 90)
        fish._energy = 95
        self.assertEqual(fish.status(), AnimalStatus.FULL)
        fish._energy = 100
        self.assertEqual(fish.status(), AnimalStatus.FULL)

    def test_update(self):

        fish = Mackerel(start_energy=5, max_energy=100)

        result = fish.update()
        self.assertEqual(fish._energy, 4)
        self.assertTrue(result)


        fish._energy = 1
        result = fish.update()

        self.assertEqual(fish._energy, 0)
        self.assertFalse(result)

        with self.assertRaises(AnimalException):
            fish.update()


    def test_fish_eat(self):
        """Tests the fish eat function"""
        fish = Mackerel(start_energy=20, max_energy=100)

        fish._max_energy = fish._MAX_ENERGY
        fish.eat(30)
        self.assertEqual(fish._energy, 50)
        fish.eat(100)
        self.assertEqual(fish._energy, 100)

    def test_mammal_eat(self):

        """Tests the mammal eat function"""

        mammal = Tiger(start_energy=20, max_energy=100)

        mammal._max_energy = mammal._MAX_ENERGY
        mammal.eat(30)
        self.assertEqual(mammal._energy, 35)

    # def test_Animal(self):
    #     a = Animal()

    # def test_Mammal(self):
    #     a = Mammal()

    # def test_Fish(self):
    #     a = Fish()

    # def test_Cat(self):
    #     a = Cat()

    # def test_Primate(self):
    #     a = Primate()


if __name__ == '__main__':
    unittest.main()
