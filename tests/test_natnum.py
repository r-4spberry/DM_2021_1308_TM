import sys
import os
import random
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
        self.assertEqual(nat_mul_by_digit(natural_number(10), 0),
                         natural_number(0))
        self.assertEqual(nat_mul_by_digit(natural_number(2), 2),
                         natural_number(4))
        self.assertEqual(nat_mul_by_digit(natural_number(8), 2),
                         natural_number(16))
        self.assertEqual(nat_mul_by_digit(natural_number(7), 1),
                         natural_number(7))
        self.assertEqual(nat_mul_by_digit(natural_number(0), 9),
                         natural_number(0))
        
        self.assertRaises(TypeError, nat_mul_by_digit, natural_number(1), "s")
        self.assertRaises(TypeError, nat_mul_by_digit, "s", 3)
        self.assertRaises(ValueError, nat_mul_by_digit, natural_number(1), 15)
        self.assertRaises(ValueError, nat_mul_by_digit, natural_number(1), -5)
        
    def test_mul_by_10_pow(self):
        self.assertEqual(nat_mul_by_10_pow(natural_number(3), 3), 
                         natural_number(3000))
        self.assertEqual(nat_mul_by_10_pow(natural_number(3), natural_number(3)), 
                         natural_number(3000))
        self.assertEqual(nat_mul_by_10_pow(natural_number(0), 3), 
                         natural_number(0))
        self.assertEqual(nat_mul_by_10_pow(natural_number(44), 3), 
                         natural_number(44000))
        
        
        self.assertRaises(TypeError, nat_mul_by_10_pow, natural_number(1), "s")
        self.assertRaises(TypeError, nat_mul_by_10_pow, "s", natural_number(1))
    
    def test_mul(self):
        self.assertRaises(TypeError, nat_mul, natural_number(1), "s")
        self.assertRaises(TypeError, nat_mul, "s", natural_number(1))
        
        self.assertEqual(nat_mul(natural_number(12345679), natural_number(27)), 
                         natural_number(333333333))
        self.assertEqual(nat_mul(natural_number(12345679), natural_number(0)), 
                         natural_number(0))
        self.assertEqual(nat_mul(natural_number(0), natural_number(27)), 
                         natural_number(0))
        self.assertEqual(nat_mul(natural_number(12345679), natural_number(1)), 
                         natural_number(12345679))
        
    def test_sub_mul(self):
        self.assertRaises(TypeError, SUB_NDN_N, natural_number(1), "s", 1)
        self.assertRaises(TypeError, SUB_NDN_N, "s", natural_number(1), 1)
        self.assertRaises(ValueError, SUB_NDN_N, natural_number(1), natural_number(1), 15)
        self.assertRaises(ValueError, SUB_NDN_N, natural_number(1), natural_number(1), -15)
        self.assertRaises(ValueError, SUB_NDN_N, natural_number(1), natural_number(1), 5)
        
        self.assertEqual(SUB_NDN_N(natural_number(100), natural_number(5), 6), natural_number(70))
        self.assertEqual(SUB_NDN_N(natural_number(101), natural_number(5), 1), natural_number(96))
        self.assertEqual(SUB_NDN_N(natural_number(100), natural_number(5), 0), natural_number(100))
        self.assertEqual(SUB_NDN_N(natural_number(100), natural_number(0), 6), natural_number(100))
        self.assertEqual(SUB_NDN_N(natural_number(0), natural_number(5), 0), natural_number(0))
        self.assertEqual(SUB_NDN_N(natural_number(0), natural_number(0), 0), natural_number(0))
    
    def test_DIV_NN_Dk(self):
        self.assertRaises(TypeError, DIV_NN_Dk, natural_number(1), "s")
        self.assertRaises(TypeError, DIV_NN_Dk, "s", natural_number(1))
        self.assertRaises(ValueError, DIV_NN_Dk, natural_number(2), natural_number(10))
        
        self.assertEqual(DIV_NN_Dk(natural_number(123456), natural_number(432)), 200)
        self.assertEqual(DIV_NN_Dk(natural_number(123456), natural_number(123456)), 1)
        self.assertEqual(DIV_NN_Dk(natural_number(123456), natural_number(123455)), 1)
        self.assertEqual(DIV_NN_Dk(natural_number(10), natural_number(2)), 5)
        
        n1 = natural_number(random.randrange(434, 35234))
        d = 5435
        n2 = nat_mul(n1, natural_number(d))
        self.assertEqual(DIV_NN_Dk(n2, n1), 5000)
    
    def test_nat_div(self):
        self.assertRaises(TypeError, nat_div, natural_number(1), "s")
        self.assertRaises(TypeError, nat_div, "s", natural_number(1))
        self.assertRaises(ValueError, nat_div, natural_number(2), natural_number(10))
        
        self.assertEqual(nat_div(natural_number(123456), natural_number(432)), 285)
        self.assertEqual(nat_div(natural_number(123456), natural_number(123456)), 1)
        self.assertEqual(nat_div(natural_number(123456), natural_number(123455)), 1)
        self.assertEqual(nat_div(natural_number(10), natural_number(2)), 5)
        self.assertEqual(nat_div(natural_number(13), natural_number(2)), 6)
        n1 = natural_number(random.randrange(434, 35234))
        d = 5435
        n2 = nat_mul(n1, natural_number(d))
        n2 = nat_sum(n2, natural_number(15))
        self.assertEqual(nat_div(n2, n1), d)
        self.assertEqual(nat_div(n1, natural_number(1)), n1)

    def test_nat_mod(self):
        self.assertRaises(TypeError, nat_mod, natural_number(1), "s")
        self.assertRaises(TypeError, nat_mod, "s", natural_number(1))
        self.assertRaises(ValueError, nat_mod, natural_number(2), natural_number(10))
        
        self.assertEqual(nat_mod(natural_number(123456), natural_number(432)), 336)
        self.assertEqual(nat_mod(natural_number(123456), natural_number(1)), 0)
        self.assertEqual(nat_mod(natural_number(123456), natural_number(123456)), 0)
        self.assertEqual(nat_mod(natural_number(123456), natural_number(123455)), 1)
        self.assertEqual(nat_mod(natural_number(10), natural_number(2)), 0)
        self.assertEqual(nat_mod(natural_number(13), natural_number(2)), 1)
        n1 = natural_number(random.randrange(434, 35234))
        d = 5435
        n2 = nat_mul(n1, natural_number(d))
        n2 = nat_sum(n2, natural_number(15))
        self.assertEqual(nat_mod(n2, n1), 15)
        
    def test_gcd(self):
        self.assertEqual(nat_gcd(natural_number(1), natural_number(1)), 1)
        self.assertEqual(nat_gcd(natural_number(33), natural_number(33)), 33)
        self.assertEqual(nat_gcd(natural_number(124), natural_number(16)), 4)
        self.assertEqual(nat_gcd(natural_number(15), natural_number(0)), 0)
        self.assertEqual(nat_gcd(natural_number(363), natural_number(3)), 3)

    def test_lcm(self):
        self.assertEqual(nat_lcm(natural_number(1), natural_number(1)), 1)
        self.assertEqual(nat_lcm(natural_number(124), natural_number(16)), 496)
        self.assertRaises(ValueError, nat_lcm, natural_number(15), natural_number(0))
        self.assertEqual(nat_lcm(natural_number(363), natural_number(3)), 363)
    
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
