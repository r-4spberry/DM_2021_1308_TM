import sys
import os
import random
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from integer import *
from natnum import *
class TestInt(unittest.TestCase):
    def test_nat_init2(self):
        Integer(0)
        Integer("123")
        Integer(-7)
        Integer("-15")
        self.assertRaises(ValueError, Integer, "-1 10")
        self.assertRaises(TypeError, Integer, 1.0)
    def test_nat_is_zero(self):
        self.assertTrue(Integer(0).is_zero())
        self.assertFalse(Integer(1).is_zero())
        self.assertFalse(Integer(-2).is_zero())
    def test_nat_abs(self):
        self.assertEqual(ABS_Z_N(Integer(5)),NaturalNumber(5))
        self.assertEqual(ABS_Z_N(Integer(-5)), NaturalNumber(5))
        self.assertEqual(ABS_Z_N(Integer(0)), NaturalNumber(0))
    def test_nat_poz(self):
        self.assertEqual(POZ_Z_D(Integer(-5)), int(1))
        self.assertEqual(POZ_Z_D(Integer(5)), int(2))
        self.assertEqual(POZ_Z_D(Integer(0)), int(0))
    def test_nat_mulm(self):
        self.assertEqual(MUL_ZM_Z(Integer(-5)), Integer(5))
        self.assertEqual(MUL_ZM_Z(Integer(5)), Integer(-5))
    def test_nat_transnz(self):
        self.assertEqual(TRANS_N_Z(NaturalNumber(5)), Integer(5))
        self.assertRaises(TypeError, TRANS_N_Z, -1)
        self.assertRaises(TypeError, TRANS_N_Z, "-1")
    def test_nat_transzn(self):
        self.assertEqual(TRANS_Z_N(Integer(5)),  NaturalNumber(5))
    def test_nat_add(self):
        self.assertEqual(ADD_ZZ_Z(Integer(5),Integer(5)), Integer(10))
        self.assertEqual(ADD_ZZ_Z(Integer(5), Integer(-5)), Integer(0))
        self.assertEqual(ADD_ZZ_Z(Integer(-5), Integer(-5)), Integer(-10))
        self.assertEqual(ADD_ZZ_Z(Integer(-12), Integer(5)), Integer(-7))
        self.assertEqual(ADD_ZZ_Z(Integer(-5), Integer(7)), Integer(2))
    def test_nat_sub(self):
        self.assertEqual(SUB_ZZ_Z(Integer(5), Integer(5)), Integer(0))
        self.assertEqual(SUB_ZZ_Z(Integer(5), Integer(10)), Integer(-5))
        self.assertEqual(SUB_ZZ_Z(Integer(2), Integer(-2)), Integer(4))
        self.assertEqual(SUB_ZZ_Z(Integer(-5), Integer(10)), Integer(-15))
    def test_nat_mulz(self):
        self.assertEqual(MUL_ZZ_Z(Integer(5), Integer(5)), Integer(25))
        self.assertEqual(MUL_ZZ_Z(Integer(5), Integer(0)), Integer(0))
        self.assertEqual(MUL_ZZ_Z(Integer(-3), Integer(-3)), Integer(9))
        self.assertEqual(MUL_ZZ_Z(Integer(-3), Integer(5)), Integer(-15))
    def test_nat_div(self):
        self.assertEqual(DIV_ZZ_Z(Integer(25), Integer(5)), Integer(5))
        self.assertEqual(DIV_ZZ_Z(Integer(-25), Integer(5)), Integer(-5))
        self.assertEqual(DIV_ZZ_Z(Integer(25), Integer(-5)), Integer(-5))
        self.assertEqual(DIV_ZZ_Z(Integer(-25), Integer(-5)), Integer(5))
        self.assertEqual(DIV_ZZ_Z(Integer(0), Integer(5)), Integer(0))
        self.assertEqual(DIV_ZZ_Z(Integer(5), Integer(10)), Integer(0))
        self.assertEqual(DIV_ZZ_Z(Integer(-13), Integer(4)), Integer(-4))
    def test_nat_mod(self):
        self.assertEqual(MOD_ZZ_Z(Integer(25), Integer(5)), Integer(0))
        self.assertEqual(MOD_ZZ_Z(Integer(12), Integer(5)), Integer(2))
        self.assertEqual(MOD_ZZ_Z(Integer(-12), Integer(5)), Integer(3))
        self.assertEqual(MOD_ZZ_Z(Integer(-12), Integer(-5)), Integer(3))
        self.assertEqual(MOD_ZZ_Z(Integer(12), Integer(-5)), Integer(2))







def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
