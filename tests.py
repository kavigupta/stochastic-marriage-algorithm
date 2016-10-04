
import unittest

from prefs import Preferences

from random import randint, sample

class PreferenceTests(unittest.TestCase):
    def test_prefs(self):
        p = Preferences([1, 2, 3, 4, 5])
        self.assertTrue(p.prefers(1, 2))
        self.assertFalse(p.prefers(2, 1))
        self.assertTrue(p.prefers(2, 5))
        self.assertTrue(p.prefers(2, 3))
        self.assertTrue(p.prefers(1, 5))
        self.assertFalse(p.prefers(5, 1))
        self.assertFalse(p.prefers(5, 5))
        self.assertEqual([1,2,3,4,5], list(p))
    def test_pref_rankings(self):
        total = list(range(0,1000))
        for _ in range(1000):
            samp = sample(total, randint(20, 700))
            self.assertEqual(samp, list(Preferences(samp)))

unittest.main()