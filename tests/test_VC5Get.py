from unittest import TestCase
from vec2pat import *


class TestVC5Get(TestCase):
    vc5 = VC5Get()

    def test_conf_enable(self):
        self.assertEqual(self.vc5.conf_enable, [1, 1, 0, 0])   # Config Enable

    def test_i2c_add(self):
        self.assertEqual(self.vc5.i2c_address, 'D4')

    def test_vco_mon(self):
        self.assertEqual(self.vc5.conf[0][0x11], '3F')
