import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from natnum import *

class TestNat(unittest.TestCase):
    def test_nat_is_zero(self):
        self.assertTrue(natural_number(0).is_zero())
        self.assertFalse(natural_number(1).is_zero())
        self.assertFalse(natural_number(2).is_zero())

    def test_nat_init(self):
        natural_number(0)
        natural_number("123")
        self.assertRaises(ValueError, natural_number, "-1")
        self.assertRaises(TypeError, natural_number, 1.0)
    
    def test_nat_cmp(self):
        self.assertEqual(nat_cmp(natural_number(1234), natural_number(1235)), 1)
        self.assertEqual(nat_cmp(natural_number(1235), natural_number(1234)), 2)
        self.assertEqual(nat_cmp(natural_number(1234), natural_number(1234)), 0)
        self.assertEqual(nat_cmp(natural_number(1234), natural_number(0)), 2)
        
    def test_nat_sum(self):
        self.assertEqual(nat_sum(natural_number(1234), natural_number(4321)), 
                         natural_number(5555))
        self.assertEqual(nat_sum(natural_number(9999), natural_number(1)), 
                         natural_number(10000))
        self.assertEqual(nat_sum(natural_number(1000), natural_number(0)), 
                         natural_number(1000))
        self.assertEqual(nat_sum(natural_number(0), natural_number(0)), 
                         natural_number(0))
        self.assertEqual(nat_sum(natural_number(1234), natural_number(4321)), 
                         natural_number(5555))
    
    def test_add_1(self):
        n1 = natural_number(0)
        n1.add_1()
        n2 = natural_number(999)
        n2.add_1()
        n3 = natural_number(1299)
        n3.add_1()
        
        self.assertEqual(n1, natural_number(1))
        self.assertEqual(n2, natural_number(1000))
        self.assertEqual(n3, natural_number(1300))
    
    def test_nat_sub(self):
        self.assertRaises(ValueError, nat_sub, natural_number(1), natural_number(2))
        self.assertEqual(nat_sub(natural_number(100), natural_number(1)),
                         natural_number(99))
        self.assertEqual(nat_sub(natural_number(100), natural_number(100)),
                         natural_number(0))
        self.assertEqual(nat_sub(natural_number(12345), natural_number(2345)),
                         natural_number(10000))
        
    def test_remove_leading_zeros(self):
        n1 = natural_number(1)
        n1.digits.append(0)
        n1.digits.append(0)
        n1.remove_leading_zeros()
        self.assertEqual(n1, natural_number(1))
        n2 = natural_number(0)
        n2.digits.append(0)
        n2.digits.append(0)
        n2.remove_leading_zeros()
        self.assertEqual(n2, natural_number(0))
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
