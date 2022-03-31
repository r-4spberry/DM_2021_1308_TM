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
        self.assertEqual(nat_sum(natural_number(0), natural_number(1000)), 
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
        #пытаемся вычесть из большего меньшее
        self.assertRaises(ValueError, nat_sub, natural_number(1), natural_number(2))
        
        #просто вычитаем
        self.assertEqual(nat_sub(natural_number(100), natural_number(1)),
                         natural_number(99))
        self.assertEqual(nat_sub(natural_number(100), natural_number(100)),
                         natural_number(0))
        self.assertEqual(nat_sub(natural_number(12345), natural_number(2345)),
                         natural_number(10000))
        
    def test_remove_leading_zeros(self):
        #убираем нули у 001
        n1 = natural_number(1)
        n1.digits.append(0)
        n1.digits.append(0)
        n1.remove_leading_zeros()
        self.assertEqual(n1, natural_number(1))
        
        #пытаемся убрать их у 1
        n1.remove_leading_zeros()
        self.assertEqual(n1, natural_number(1))
        
        #пытаемся убрать их у 0
        n2 = natural_number(0)
        n2.digits.append(0)
        n2.digits.append(0)
        n2.remove_leading_zeros()
        self.assertEqual(n2, natural_number(0))
    
    def test_mul_by_digit(self):
        self.assertEqual(mul_nat_by_digit(natural_number(10), 0),
                         natural_number(0))
        self.assertEqual(mul_nat_by_digit(natural_number(2), 2),
                         natural_number(4))
        self.assertEqual(mul_nat_by_digit(natural_number(8), 2),
                         natural_number(16))
        self.assertEqual(mul_nat_by_digit(natural_number(7), 1),
                         natural_number(7))
        self.assertEqual(mul_nat_by_digit(natural_number(0), 9),
                         natural_number(0))
        
        self.assertRaises(TypeError, mul_nat_by_digit, natural_number(1), "s")
        self.assertRaises(TypeError, mul_nat_by_digit, "s", 3)
        self.assertRaises(ValueError, mul_nat_by_digit, natural_number(1), 15)
        
    def test_mul_by_10_pow(self):
        self.assertEqual(mul_nat_by_10_pow(natural_number(3), 3), 
                         natural_number(3000))
        self.assertEqual(mul_nat_by_10_pow(natural_number(3), natural_number(3)), 
                         natural_number(3000))
        self.assertEqual(mul_nat_by_10_pow(natural_number(0), 3), 
                         natural_number(0))
        self.assertEqual(mul_nat_by_10_pow(natural_number(44), 3), 
                         natural_number(44000))
        
        
        self.assertRaises(TypeError, mul_nat_by_10_pow, natural_number(1), "s")
        self.assertRaises(TypeError, mul_nat_by_10_pow, "s", natural_number(1))
    
    def test_mul(self):
        self.assertRaises(TypeError, mul_nat, natural_number(1), "s")
        self.assertRaises(TypeError, mul_nat, "s", natural_number(1))
        
        self.assertEqual(mul_nat(natural_number(12345679), natural_number(27)), 
                         natural_number(333333333))
        self.assertEqual(mul_nat(natural_number(12345679), natural_number(0)), 
                         natural_number(0))
        self.assertEqual(mul_nat(natural_number(0), natural_number(27)), 
                         natural_number(0))
        self.assertEqual(mul_nat(natural_number(12345679), natural_number(1)), 
                         natural_number(12345679))
        
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
