import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from rational import *
from polynual import *


class TestInt(unittest.TestCase):
    def test_ADD_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1=Polynom([rational.RationalNumber(1,1), rational.RationalNumber(1,1), rational.RationalNumber(1,1)])
        p2=Polynom([rational.RationalNumber(1,1), rational.RationalNumber(1,1), rational.RationalNumber(1,1)])
        pres1=Polynom([rational.RationalNumber(2,1), rational.RationalNumber(2,1), rational.RationalNumber(2,1)])
        self.assertEqual(ADD_PP_P(p1,p2).__str__(),pres1.__str__())

        #---2---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(0, 1)])
        pres1=Polynom([rational.RationalNumber(2,1), rational.RationalNumber(2,1), rational.RationalNumber(1,1)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(0, 1), rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(3, 2), rational.RationalNumber(9, 1), rational.RationalNumber(1, 2)])
        pres1 = Polynom([RationalNumber(5,2), RationalNumber(9,1), RationalNumber(13,2)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1)])
        p2 = Polynom([rational.RationalNumber(5, 8), rational.RationalNumber(4, 3), rational.RationalNumber(1, 2)])
        pres1 = Polynom([RationalNumber(13,8), RationalNumber(4,3), RationalNumber(1,2)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())

    def test_SUB_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(0,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(0, 1)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(1,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(0, 1), rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(3, 2), rational.RationalNumber(9, 1), rational.RationalNumber(1, 2)])
        pres1 = Polynom([RationalNumber(-1,2), RationalNumber(-9,1), RationalNumber(11,2)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1)])
        p2 = Polynom([rational.RationalNumber(5, 8), rational.RationalNumber(4, 3), rational.RationalNumber(1, 2)])
        pres1 = Polynom([RationalNumber(3,8), RationalNumber(-4,3), RationalNumber(-1,2)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())


    def test_MUL_PQ_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        x=RationalNumber(4,1)
        pres1 = Polynom([RationalNumber(4,1), RationalNumber(4,1), RationalNumber(4,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(1, 2), rational.RationalNumber(3, 4), rational.RationalNumber(7, 1)])
        x = RationalNumber(4, 7)
        pres1 = Polynom([RationalNumber(2,7), RationalNumber(3,7), RationalNumber(4,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())

        # ---3---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(22, 1), rational.RationalNumber(31, 8)])
        x = RationalNumber(0, 1)
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(0,8)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())

        # ---4---
        p1 = Polynom([rational.RationalNumber(8, 3), rational.RationalNumber(5, 2), rational.RationalNumber(4, 1)])
        x = RationalNumber(1, 2)
        pres1 = Polynom([RationalNumber(4,3), RationalNumber(5,4), RationalNumber(2,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())

    def test_MUL_Pxk_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(7, 3), rational.RationalNumber(4, 9), rational.RationalNumber(2, 3)])
        x=2
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(7,3), RationalNumber(4,9), RationalNumber(2,3)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(2, 3), rational.RationalNumber(1, 1), rational.RationalNumber(2, 2)])
        x = 1
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(2,3), RationalNumber(1,1), RationalNumber(2,2)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())

        # ---3---
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(3, 1), rational.RationalNumber(4, 1)])
        x = 0
        pres1 = Polynom([RationalNumber(2,1), RationalNumber(3,1), RationalNumber(4,1)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())

        # ---4---
        p1 = Polynom([rational.RationalNumber(25, 5), rational.RationalNumber(24, 1), rational.RationalNumber(22, 8)])
        x = 2
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(25,5), RationalNumber(24,1), RationalNumber(22,8)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())

    def test_LED_P_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(7, 3), rational.RationalNumber(4, 9), rational.RationalNumber(2, 3)])
        pres1 = RationalNumber(2,3)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))

        # ---2---
        p1 = Polynom([rational.RationalNumber(75, 3), rational.RationalNumber(44, 1), rational.RationalNumber(4, 1)])
        pres1 = RationalNumber(4, 1)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))


        # ---3---
        p1 = Polynom([rational.RationalNumber(21, 3), rational.RationalNumber(9, 10)])
        pres1 = RationalNumber(9, 10)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))

        # ---4---
        p1 = Polynom([rational.RationalNumber(-9, 7)])
        pres1 = RationalNumber(-9, 7)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))

    def test_LED_P_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(3, 5), rational.RationalNumber(12, 1), rational.RationalNumber(32, 1)])
        pres1 = 2
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

        # ---2---
        p1 = Polynom([rational.RationalNumber(12, 1), rational.RationalNumber(32, 1)])
        pres1 = 1
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

        # ---3---
        p1 = Polynom([rational.RationalNumber(32, 1)])
        pres1 = 0
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

        # ---4---
        p1 = Polynom([rational.RationalNumber(12, 1), rational.RationalNumber(0, 1), rational.RationalNumber(12, 1), rational.RationalNumber(32, 1),
                      rational.RationalNumber(12, 1), rational.RationalNumber(32, 1)])
        pres1 = 5
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

    def test_FAC_P_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(3, 5), rational.RationalNumber(6, 15), rational.RationalNumber(9, 10)])
        pres1 = RationalNumber(18,5)
        pres2 = Polynom([RationalNumber(1,6), RationalNumber(1,9), RationalNumber(1,4)])
        p,P=FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

        # ---2---
        p1 = Polynom([rational.RationalNumber(2, 7), rational.RationalNumber(6, 14), rational.RationalNumber(8, 7)])
        pres1 = RationalNumber(24,7)
        pres2 = Polynom([RationalNumber(1,12), RationalNumber(1,8), RationalNumber(1,3)])
        p, P = FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

        # ---3---
        p1 = Polynom([rational.RationalNumber(4, 7), rational.RationalNumber(6, 14), rational.RationalNumber(7, 3)])
        pres1 = RationalNumber(84,1)
        pres2 = Polynom([RationalNumber(1,147), RationalNumber(1,196), RationalNumber(1,36)])
        p, P = FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

        # ---4---
        p1 = Polynom([rational.RationalNumber(1, 9), rational.RationalNumber(8, 18), rational.RationalNumber(3, 3), rational.RationalNumber(5, 6)])
        pres1 = RationalNumber(120,3)
        pres2 = Polynom([RationalNumber(1,360), RationalNumber(1,90), RationalNumber(1,40), RationalNumber(1,48)])
        p, P = FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

    def test_MUL_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(1, 9), rational.RationalNumber(8, 18), rational.RationalNumber(3, 3)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1,9), RationalNumber(5,9), RationalNumber(14,9), RationalNumber(13,9), RationalNumber(1,1)])
        self.assertEqual(MUL_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(1, 9), rational.RationalNumber(0, 18), rational.RationalNumber(0, 3)])
        p2 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(2,9), RationalNumber(1,9), RationalNumber(1,3), RationalNumber(0,18), RationalNumber(0,3)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3---
        p1 = Polynom([rational.RationalNumber(0, 18), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(0,18), RationalNumber(1,1), RationalNumber(3,1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---4---
        p1 = Polynom([rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1)])
        pres1=Polynom([RationalNumber(3,1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

    def test_DIV_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(-8,1), RationalNumber(3,1)])
        self.assertEqual(DIV_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(46,1), RationalNumber(-15,1), RationalNumber(6,1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---3---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(1,3), RationalNumber(1,3), RationalNumber(1,1), RationalNumber(2,1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---4---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),
                      rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),
                      rational.RationalNumber(6, 1)])
        pres1 = Polynom([RationalNumber(1,1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

    def test_MOD_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(25,1)])
        self.assertEqual(MOD_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(-137,1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---3---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1)])
        pres1 = Polynom([])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---4---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),
                      rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),
                      rational.RationalNumber(6, 1)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(0,1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

    def test_GCF_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),
                      rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(2,3), RationalNumber(-4,3)])
        self.assertEqual(GCF_PP_P(p1,p2).__str__(),pres1.__str__())

    def test_DER_P_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1---
        p1 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(1, 3),
                      rational.RationalNumber(6, 3)])
        pres1 = Polynom([RationalNumber(6,1), RationalNumber(1,3)])
        self.assertEqual(DER_P_P(p1).__str__(),pres1.__str__())

        # ---2---
        p1 = Polynom([rational.RationalNumber(1, 3), rational.RationalNumber(1, 3), rational.RationalNumber(1, 3),
                      rational.RationalNumber(6, 7)])
        pres1 = Polynom([RationalNumber(1,1), RationalNumber(2,3), RationalNumber(1,3)])
        self.assertEqual(DER_P_P(p1).__str__(), pres1.__str__())

        # ---3---
        p1 = Polynom([rational.RationalNumber(1, 8),rational.RationalNumber(1, 8),rational.RationalNumber(1, 8),rational.RationalNumber(1, 8), rational.RationalNumber(2, 3), rational.RationalNumber(1, 3),  rational.RationalNumber(2, 19),
                      rational.RationalNumber(6, 7)])
        pres1 = Polynom([RationalNumber(7,8), RationalNumber(3,4), RationalNumber(5,8), RationalNumber(1,2), RationalNumber(2,1), RationalNumber(2,3), RationalNumber(2,19)])
        self.assertEqual(DER_P_P(p1).__str__(), pres1.__str__())



        # ---4---




def main():
    unittest.main()


if __name__ == "__main__":
    main()