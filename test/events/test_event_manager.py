
import unittest
from src.events.events import *
from src.events.event_manager import *
from src.zoo.animals import *

class TestZoo(unittest.TestCase):

    def test_register(self):

        manager = EventManager()

        l = Lion(start_energy=60, max_energy=100)
        event1 = OneTimeEvent(10, l, l.eat, 1)
        event2 = OneTimeEvent(20, l, l.eat, 1)
        event3 = OneTimeEvent(20, l, l.eat, 1)
        event4 = OneTimeEvent(30, l, l.eat, 1)

        manager.register(event1)
        manager.register(event2)
        manager.register(event3)
        manager.register(event4)

        self.assertEqual(manager._eventlist[0], event1)
        self.assertNotEqual(manager._eventlist[0], event2)
