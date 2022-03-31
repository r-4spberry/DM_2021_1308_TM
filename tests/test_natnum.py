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
        self.assertTrue(NaturalNumber(0).is_zero())
        self.assertFalse(NaturalNumber(1).is_zero())
        self.assertFalse(NaturalNumber(2).is_zero())

    def test_nat_init(self):
        NaturalNumber(0)
        NaturalNumber("123")
        self.assertRaises(ValueError, NaturalNumber, "-1")
        self.assertRaises(TypeError, NaturalNumber, 1.0)
    
    def test_nat_cmp(self):
        self.assertEqual(nat_cmp(NaturalNumber(1234), NaturalNumber(1235)), 1)
        self.assertEqual(nat_cmp(NaturalNumber(1235), NaturalNumber(1234)), 2)
        self.assertEqual(nat_cmp(NaturalNumber(1234), NaturalNumber(1234)), 0)
        self.assertEqual(nat_cmp(NaturalNumber(1234), NaturalNumber(0)), 2)
        
    def test_nat_sum(self):
        self.assertEqual(nat_sum(NaturalNumber(1234), NaturalNumber(4321)), 
                         NaturalNumber(5555))
        self.assertEqual(nat_sum(NaturalNumber(9999), NaturalNumber(1)), 
                         NaturalNumber(10000))
        self.assertEqual(nat_sum(NaturalNumber(0), NaturalNumber(1000)), 
                         NaturalNumber(1000))
        self.assertEqual(nat_sum(NaturalNumber(0), NaturalNumber(0)), 
                         NaturalNumber(0))
        self.assertEqual(nat_sum(NaturalNumber(1234), NaturalNumber(4321)), 
                         NaturalNumber(5555))
    
    def test_add_1(self):
        n1 = NaturalNumber(0)
        n1.add_1()
        n2 = NaturalNumber(999)
        n2.add_1()
        n3 = NaturalNumber(1299)
        n3.add_1()

        self.assertEqual(n1, NaturalNumber(1))
        self.assertEqual(n2, NaturalNumber(1000))
        self.assertEqual(n3, NaturalNumber(1300))
    
    def test_nat_sub(self):
        #пытаемся вычесть из большего меньшее
        self.assertRaises(ValueError, nat_sub, NaturalNumber(1), NaturalNumber(2))
        
        #просто вычитаем
        self.assertEqual(nat_sub(NaturalNumber(100), NaturalNumber(1)),
                         NaturalNumber(99))
        self.assertEqual(nat_sub(NaturalNumber(100), NaturalNumber(100)),
                         NaturalNumber(0))
        self.assertEqual(nat_sub(NaturalNumber(12345), NaturalNumber(2345)),
                         NaturalNumber(10000))
        
    def test_remove_leading_zeros(self):
        #убираем нули у 001
        n1 = NaturalNumber(1)
        n1.digits.append(0)
        n1.digits.append(0)
        n1.remove_leading_zeros()
        self.assertEqual(n1, NaturalNumber(1))
        
        #пытаемся убрать их у 1
        n1.remove_leading_zeros()
        self.assertEqual(n1, NaturalNumber(1))
        
        #пытаемся убрать их у 0
        n2 = NaturalNumber(0)
        n2.digits.append(0)
        n2.digits.append(0)
        n2.remove_leading_zeros()
        self.assertEqual(n2, NaturalNumber(0))
    
    def test_mul_by_digit(self):
        self.assertEqual(nat_mul_by_digit(NaturalNumber(10), 0),
                         NaturalNumber(0))
        self.assertEqual(nat_mul_by_digit(NaturalNumber(2), 2),
                         NaturalNumber(4))
        self.assertEqual(nat_mul_by_digit(NaturalNumber(8), 2),
                         NaturalNumber(16))
        self.assertEqual(nat_mul_by_digit(NaturalNumber(7), 1),
                         NaturalNumber(7))
        self.assertEqual(nat_mul_by_digit(NaturalNumber(0), 9),
                         NaturalNumber(0))
        
        self.assertRaises(TypeError, nat_mul_by_digit, NaturalNumber(1), "s")
        self.assertRaises(TypeError, nat_mul_by_digit, "s", 3)
        self.assertRaises(ValueError, nat_mul_by_digit, NaturalNumber(1), 15)
        self.assertRaises(ValueError, nat_mul_by_digit, NaturalNumber(1), -5)
        
    def test_mul_by_10_pow(self):
        self.assertEqual(nat_mul_by_10_pow(NaturalNumber(3), 3), 
                         NaturalNumber(3000))
        self.assertEqual(nat_mul_by_10_pow(NaturalNumber(3), NaturalNumber(3)), 
                         NaturalNumber(3000))
        self.assertEqual(nat_mul_by_10_pow(NaturalNumber(0), 3), 
                         NaturalNumber(0))
        self.assertEqual(nat_mul_by_10_pow(NaturalNumber(44), 3), 
                         NaturalNumber(44000))
        
        
        self.assertRaises(TypeError, nat_mul_by_10_pow, NaturalNumber(1), "s")
        self.assertRaises(TypeError, nat_mul_by_10_pow, "s", NaturalNumber(1))
    
    def test_mul(self):
        self.assertRaises(TypeError, nat_mul, NaturalNumber(1), "s")
        self.assertRaises(TypeError, nat_mul, "s", NaturalNumber(1))
        
        self.assertEqual(nat_mul(NaturalNumber(12345679), NaturalNumber(27)), 
                         NaturalNumber(333333333))
        self.assertEqual(nat_mul(NaturalNumber(12345679), NaturalNumber(0)), 
                         NaturalNumber(0))
        self.assertEqual(nat_mul(NaturalNumber(0), NaturalNumber(27)), 
                         NaturalNumber(0))
        self.assertEqual(nat_mul(NaturalNumber(12345679), NaturalNumber(1)), 
                         NaturalNumber(12345679))
        
    def test_sub_mul(self):
        self.assertRaises(TypeError, SUB_NDN_N, NaturalNumber(1), "s", 1)
        self.assertRaises(TypeError, SUB_NDN_N, "s", NaturalNumber(1), 1)
        self.assertRaises(ValueError, SUB_NDN_N, NaturalNumber(1), NaturalNumber(1), 15)
        self.assertRaises(ValueError, SUB_NDN_N, NaturalNumber(1), NaturalNumber(1), -15)
        self.assertRaises(ValueError, SUB_NDN_N, NaturalNumber(1), NaturalNumber(1), 5)
        
        self.assertEqual(SUB_NDN_N(NaturalNumber(100), NaturalNumber(5), 6), NaturalNumber(70))
        self.assertEqual(SUB_NDN_N(NaturalNumber(101), NaturalNumber(5), 1), NaturalNumber(96))
        self.assertEqual(SUB_NDN_N(NaturalNumber(100), NaturalNumber(5), 0), NaturalNumber(100))
        self.assertEqual(SUB_NDN_N(NaturalNumber(100), NaturalNumber(0), 6), NaturalNumber(100))
        self.assertEqual(SUB_NDN_N(NaturalNumber(0), NaturalNumber(5), 0), NaturalNumber(0))
        self.assertEqual(SUB_NDN_N(NaturalNumber(0), NaturalNumber(0), 0), NaturalNumber(0))
    
    def test_DIV_NN_Dk(self):
        self.assertRaises(TypeError, DIV_NN_Dk, NaturalNumber(1), "s")
        self.assertRaises(TypeError, DIV_NN_Dk, "s", NaturalNumber(1))
        self.assertRaises(ValueError, DIV_NN_Dk, NaturalNumber(2), NaturalNumber(10))
        
        self.assertEqual(DIV_NN_Dk(NaturalNumber(123456), NaturalNumber(432)), 200)
        self.assertEqual(DIV_NN_Dk(NaturalNumber(123456), NaturalNumber(123456)), 1)
        self.assertEqual(DIV_NN_Dk(NaturalNumber(123456), NaturalNumber(123455)), 1)
        self.assertEqual(DIV_NN_Dk(NaturalNumber(10), NaturalNumber(2)), 5)
        
        n1 = NaturalNumber(random.randrange(434, 35234))
        d = 5435
        n2 = nat_mul(n1, NaturalNumber(d))
        self.assertEqual(DIV_NN_Dk(n2, n1), 5000)
    
    def test_nat_div(self):
        self.assertRaises(TypeError, nat_div, NaturalNumber(1), "s")
        self.assertRaises(TypeError, nat_div, "s", NaturalNumber(1))
        self.assertRaises(ValueError, nat_div, NaturalNumber(2), NaturalNumber(10))
        
        self.assertEqual(nat_div(NaturalNumber(123456), NaturalNumber(432)), 285)
        self.assertEqual(nat_div(NaturalNumber(123456), NaturalNumber(123456)), 1)
        self.assertEqual(nat_div(NaturalNumber(123456), NaturalNumber(123455)), 1)
        self.assertEqual(nat_div(NaturalNumber(10), NaturalNumber(2)), 5)
        self.assertEqual(nat_div(NaturalNumber(13), NaturalNumber(2)), 6)
        n1 = NaturalNumber(random.randrange(434, 35234))
        d = 5435
        n2 = nat_mul(n1, NaturalNumber(d))
        n2 = nat_sum(n2, NaturalNumber(15))
        self.assertEqual(nat_div(n2, n1), d)
        self.assertEqual(nat_div(n1, NaturalNumber(1)), n1)

    def test_nat_mod(self):
        self.assertRaises(TypeError, nat_mod, NaturalNumber(1), "s")
        self.assertRaises(TypeError, nat_mod, "s", NaturalNumber(1))
        self.assertRaises(ValueError, nat_mod, NaturalNumber(2), NaturalNumber(10))
        
        self.assertEqual(nat_mod(NaturalNumber(123456), NaturalNumber(432)), 336)
        self.assertEqual(nat_mod(NaturalNumber(123456), NaturalNumber(1)), 0)
        self.assertEqual(nat_mod(NaturalNumber(123456), NaturalNumber(123456)), 0)
        self.assertEqual(nat_mod(NaturalNumber(123456), NaturalNumber(123455)), 1)
        self.assertEqual(nat_mod(NaturalNumber(10), NaturalNumber(2)), 0)
        self.assertEqual(nat_mod(NaturalNumber(13), NaturalNumber(2)), 1)
        n1 = NaturalNumber(random.randrange(434, 35234))
        d = 5435
        n2 = nat_mul(n1, NaturalNumber(d))
        n2 = nat_sum(n2, NaturalNumber(15))
        self.assertEqual(nat_mod(n2, n1), 15)
        
    def test_gcd(self):
        self.assertEqual(nat_gcd(NaturalNumber(1), NaturalNumber(1)), 1)
        self.assertEqual(nat_gcd(NaturalNumber(33), NaturalNumber(33)), 33)
        self.assertEqual(nat_gcd(NaturalNumber(124), NaturalNumber(16)), 4)
        self.assertEqual(nat_gcd(NaturalNumber(15), NaturalNumber(0)), 0)
        self.assertEqual(nat_gcd(NaturalNumber(363), NaturalNumber(3)), 3)

    def test_lcm(self):
        self.assertEqual(nat_lcm(NaturalNumber(1), NaturalNumber(1)), 1)
        self.assertEqual(nat_lcm(NaturalNumber(124), NaturalNumber(16)), 496)
        self.assertRaises(ValueError, nat_lcm, NaturalNumber(15), NaturalNumber(0))
        self.assertEqual(nat_lcm(NaturalNumber(363), NaturalNumber(3)), 363)
    
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
