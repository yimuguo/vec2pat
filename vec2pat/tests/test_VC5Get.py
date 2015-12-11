from unittest import TestCase
from vec2pat import *


class TestVC5Get(TestCase):
    vc5 = VC5Get()

    def test_conf_enable(self):
        self.assertEqual(self.vc5.conf_enable, [1, 1, 0, 0])   # Config Enable

    def test_i2c_add(self):
        self.assertEqual(self.vc5.i2c_address, 'D4')

    def test_vco_mon(self):
        for x in range(0, 3):
            self.assertEqual(self.vc5.conf[x][0x11], '3F')
            self.assertEqual(int(self.vc5.conf[x][0x1d], 16) & 0b00000010, 0)
            self.assertEqual(int(self.vc5.conf[x][0x1c], 16) & 0b10000000, 0)
            self.assertEqual(int(self.vc5.conf[x][0x16], 16) & 0b00001000, 0)
