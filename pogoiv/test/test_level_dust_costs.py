import unittest
from pogoiv.cp_multipliers import CpMultipliers


class TestLevelDustCosts(unittest.TestCase):
    def tests_get_multiplier(self):
        base_stats = CpMultipliers()
        multiplier = base_stats.get_cp_multiplier(10)
        self.assertEquals(0.4225, multiplier)

    def tests_get_multiplier_odd(self):
        base_stats = CpMultipliers()
        multiplier = base_stats.get_cp_multiplier(10.5)
        self.assertEquals(0.4335117, multiplier)

