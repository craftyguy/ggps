
import json
import unittest

import m26


class AgeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def write_tmp_file(self, basename, contents):
        with open('tmp/' + basename, 'w', encoding='utf-8') as out:
            out.write(contents)
            print('tmp/ file written: ' + basename)

    def test_constructor(self):
        self.assertTrue(m26.Age().value == 0, "value should be 0")
        self.assertTrue(m26.Age().value == 0, "value should be 0")
        self.assertTrue(m26.Age(58.1).value == 58.1, "value should be 58.1")
        self.assertTrue(m26.Age('58.2').value == 58.2, "value should be 58.2")

    def test_max_pulse(self):
        self.assertTrue(m26.Age(16).max_pulse() == 200.0, "value should be 200.0")
        self.assertTrue(m26.Age(20).max_pulse() == 200.0, "value should be 200.0")
        self.assertTrue(m26.Age(21).max_pulse() == 199.0, "value should be 199.0")
        self.assertTrue(m26.Age(58.1).max_pulse() == 161.9, "value should be 161.9")

    def test_add(self):
        a16 = m26.Age(16.0)
        a58 = m26.Age(58.0)
        self.assertTrue(a58.add(a16) == 74.0, "value should be 74.0")
        self.assertTrue(a58.value == 74.0, "value should be 74.0")

    def test_subtract(self):
        a16 = m26.Age(16.0)
        a58 = m26.Age(58.0)
        self.assertTrue(a58.subtract(a16) == 42.0, "value should be 42.0")
        self.assertTrue(a58.value == 42.0, "value should be 42.0")

    def test_training_zones(self):
        a58 = m26.Age(58.0)
        zones = a58.training_zones()
        self.write_tmp_file('training_zones.json', json.dumps(zones, indent=True))
        self.assertTrue(len(zones) == 5, "there should be 5 zones")
        z0 = zones[0]
        z4 = zones[4]

        self.assertTrue(z0['pct_max'] == 0.95, "pct_max should be 0.95")
        self.assertTrue(z0['pulse']   == 153.9, "pulse should be 153.9")

        self.assertTrue(z4['pct_max'] == 0.75, "pct_max should be 0.75")
        self.assertTrue(z4['pulse']   == 121.5, "pulse should be 121.5")
