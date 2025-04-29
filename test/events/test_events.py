
import unittest
from src.events.events import *
from src.zoo.animals import *

class TestZoo(unittest.TestCase):

    def test_one_time_event_should_enovke(self):

        l = Lion(start_energy=60, max_energy=100)
        event = OneTimeEvent(30, l, l.eat, 1)
        self.assertEqual(event._start_time, 30)
        self.assertEqual(event._animal, l)
        self.assertEqual(event._action, l.eat)

        self.assertFalse(event.should_invoke(10))
        self.assertTrue(event.should_invoke(30))


    def test_recurring_event_should_invoke(self):

        l = Lion(start_energy=30, max_energy=100)
        period = 5
        reps = 1

        event = RecurringEvent(30, l, l.eat, period, reps, 1)
        self.assertEqual(event._start_time, 30)
        self.assertEqual(event._animal, l)
        self.assertEqual(event._action, l.eat)
        self.assertEqual(event._period, 5)

        self.assertTrue(event.should_invoke(35))
        self.assertFalse(event.should_invoke(36))
        self.assertTrue(event.should_invoke(40))

    def test_event_comparison(self):
        """Test the comparison methods of Event objects"""

        # Create test events with different start times
        l = Lion(start_energy=60, max_energy=100)
        event1 = OneTimeEvent(10, l, l.eat, 1)
        event2 = OneTimeEvent(20, l, l.eat, 1)
        event3 = OneTimeEvent(20, l, l.eat, 1)

        # Test less than comparison
        self.assertTrue(event1 < event2)
        self.assertFalse(event2 < event1)
        self.assertFalse(event2 < event3)

        # Test equality comparison
        self.assertTrue(event2 == event3)
        self.assertFalse(event1 == event2)

        # Test inequality comparison
        self.assertTrue(event1 != event2)
        self.assertFalse(event2 != event3)
