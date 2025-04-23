
import unittest
from src.zoo.zoo import *

class TestZoo(unittest.TestCase):

    def test_add_animal(self) -> None:

        zoo = Zoo()
        lion = Lion(start_energy=10, max_energy=30)
        zoo.add_animal("Leo", lion)

        self.assertIn("Leo", zoo._animals)

        tiger = Tiger(start_energy=80, max_energy=100)
        result = zoo.add_animal("Tiger1", tiger)
        self.assertTrue(result)

        lion2 = Lion(start_energy=80, max_energy=100)
        result_duplicate = zoo.add_animal("Tiger1", lion2)
        self.assertFalse(result_duplicate)

    def test_remove_animal(self) -> None:

        zoo = Zoo()
        mackerel = Mackerel(start_energy=30, max_energy=130)
        names = ["Trout", "Goldenfish"]

        for name in names:
            zoo.add_animal(name, mackerel)
            self.assertIn(name, zoo._animals)

            zoo.remove_animal(name)
            self.assertNotIn(name, zoo._animals)


        self.assertNotIn("Chimp", zoo._animals)

    def test_get_animal(self) -> None:

        zoo = Zoo()
        tiger = Tiger(start_energy=10, max_energy=100)
        zoo.add_animal("Teo", tiger)
        zoo.add_animal("cub", tiger)

        self.assertEqual(zoo.get_animal("Teo"), tiger)
        self.assertEqual(zoo.get_animal("cub"), tiger)

        with self.assertRaises(KeyError):
            self.assertEqual(zoo.get_animal("simba"), tiger)

        gorilla = Gorilla(start_energy=70, max_energy=100)
        zoo.add_animal("Gorilla1", gorilla)
        animal = zoo.get_animal("Gorilla1")

        self.assertIs(animal, gorilla)
        with self.assertRaises(KeyError):
            zoo.get_animal("NonExistent")

    def test_status(self):
        zoo = Zoo()

        lion = Lion(start_energy=40, max_energy=50)
        zoo.add_animal("leo", lion)

        self.assertEqual(zoo._animals["leo"].status(), AnimalStatus.NORMAL)

    def test_update(self):

        zoo = Zoo()

        # teo = Tiger(start_energy=34, max_energy=90)
        # zoo.add_animal("Teo", teo)
        # self.assertEqual(zoo.update(), [])


        # simba = Tiger(start_energy=1, max_energy=90)
        # zoo.add_animal("Simba", simba)
        # self.assertEqual(zoo.update(), [("Simba", simba)])

        tiger = Tiger(start_energy=1, max_energy=100)
        zoo.add_animal("Tiger1", tiger)
        perished = zoo.update()

        self.assertEqual(len(perished), 1)
        self.assertFalse("Tiger1" in zoo)

    def test_contains(self):

        zoo = Zoo()
        leo = Lion(start_energy=30, max_energy=60)

        zoo.add_animal("scratch", leo)

        for name in zoo._animals:
            if name == "scratch":
                self.assertTrue("scratch" in zoo)

        lion = Lion(start_energy=90, max_energy=100)
        zoo.add_animal("Lion1", lion)
        self.assertTrue("Lion1" in zoo)
        self.assertFalse("NonExistent" in zoo)


    def test_len(self):

        zoo = Zoo()

        teo = Tiger(start_energy=34, max_energy=90)
        zoo.add_animal("Teo", teo)

        simba = Tiger(start_energy=1, max_energy=90)
        zoo.add_animal("Simba", simba)

        lion = Lion(start_energy=10, max_energy=30)
        zoo.add_animal("Leo", lion)

        self.assertEqual(len(zoo), 3)

        tiger = Tiger(start_energy=80, max_energy=100)
        lion = Lion(start_energy=90, max_energy=100)

        zoo.add_animal("Tiger1", tiger)
        zoo.add_animal("Lion1", lion)

        self.assertEqual(len(zoo), 5)
        zoo.remove_animal("Tiger1")
        self.assertEqual(len(zoo), 4)



if __name__ == '__main__':
    unittest.main()
