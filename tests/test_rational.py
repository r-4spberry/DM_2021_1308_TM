import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from rational import *


class TestInt(unittest.TestCase):
    def test_RED_QQ_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])
        self.assertEqual(RED_Q_Q(RationalNumber(2, 4)).__str__(), RationalNumber(1, 2).__str__())
        self.assertEqual(RED_Q_Q(RationalNumber(21, 7)).__str__(), RationalNumber(3, 1).__str__())
        self.assertEqual(RED_Q_Q(RationalNumber(2, 4)).__str__(), RationalNumber(1, 2).__str__())
        self.assertEqual(RED_Q_Q(RationalNumber(-2, 4)).__str__(), RationalNumber(-1, 2).__str__())
        self.assertEqual(RED_Q_Q(RationalNumber(-21, 7)).__str__(), RationalNumber(-3, 1).__str__())
        self.assertEqual(RED_Q_Q(RationalNumber(0, 4)).__str__(), RationalNumber(0, 4).__str__())

    def test_INT_Q_B(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])
        self.assertEqual(INT_Q_B(RationalNumber(2, 4)), False)
        self.assertEqual(INT_Q_B(RationalNumber(0, 4)), True)
        self.assertEqual(INT_Q_B(RationalNumber(2, 2)), True)
        self.assertEqual(INT_Q_B(RationalNumber(-2, 4)), False)
        self.assertEqual(INT_Q_B(RationalNumber(-2, 1)), True)

    def test_TRANS_Z_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, RationalNumber(3, 7))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])
        self.assertEqual(TRANS_Z_Q(Integer(2)).__str__(), RationalNumber(2, 1).__str__())
        self.assertEqual(TRANS_Z_Q(Integer(0)).__str__(), RationalNumber(0, 1).__str__())
        self.assertEqual(TRANS_Z_Q(Integer(-2)).__str__(), RationalNumber(-2, 1).__str__())

    def test_TRANS_Q_Z(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])
        self.assertEqual(TRANS_Q_Z(RationalNumber(2, 1)).__str__(), Integer(2).__str__())
        self.assertEqual(TRANS_Q_Z(RationalNumber(-2, 1)).__str__(), Integer(-2).__str__())
        self.assertEqual(TRANS_Q_Z(RationalNumber(0, 4)).__str__(), Integer(0).__str__())

    def test_ADD_QQ_Q(self):
        self.assertRaises(TypeError, ADD_QQ_Q, NaturalNumber(2), NaturalNumber(3))
        self.assertRaises(TypeError, ADD_QQ_Q, Integer(3), Integer(5))
        self.assertRaises(TypeError, ADD_QQ_Q, 1.0, 5)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, ADD_QQ_Q, '10', 's')
        self.assertRaises(TypeError, ADD_QQ_Q, RationalNumber(3, 2), 's')
        self.assertEqual(ADD_QQ_Q(RationalNumber(2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(5, 2).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(1, 3), RationalNumber(1, 2)).__str__(),
                         RationalNumber(5, 6).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(2, 4), RationalNumber(1, 2)).__str__(),
                         RationalNumber(1, 1).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(-2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(-3, 2).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(2, 1), RationalNumber(-1, 2)).__str__(),
                         RationalNumber(3, 2).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(-1, 2), RationalNumber(-1, 2)).__str__(),
                         RationalNumber(-1, 1).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(1, 4), RationalNumber(-1, 4)).__str__(),
                         RationalNumber(0, 4).__str__())
        self.assertEqual(ADD_QQ_Q(RationalNumber(-1, 4), RationalNumber(1, 4)).__str__(),
                         RationalNumber(0, 4).__str__())

    def test_SUB_QQ_Q(self):
        self.assertRaises(TypeError, SUB_QQ_Q, NaturalNumber(2), NaturalNumber(3))
        self.assertRaises(TypeError, SUB_QQ_Q, Integer(3), Integer(5))
        self.assertRaises(TypeError, SUB_QQ_Q, 1.0, 5)
        self.assertRaises(TypeError, SUB_QQ_Q, '10', 's')
        self.assertRaises(TypeError, SUB_QQ_Q, RationalNumber(3, 2), 's')
        self.assertEqual(SUB_QQ_Q(RationalNumber(2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(3, 2).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(1, 3), RationalNumber(1, 2)).__str__(),
                         RationalNumber(-1, 6).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(2, 4), RationalNumber(1, 2)).__str__(),
                         RationalNumber(0, 4).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(-2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(-5, 2).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(2, 1), RationalNumber(-1, 2)).__str__(),
                         RationalNumber(5, 2).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(-1, 2), RationalNumber(-1, 2)).__str__(),
                         RationalNumber(0, 2).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(1, 4), RationalNumber(-1, 4)).__str__(),
                         RationalNumber(1, 2).__str__())
        self.assertEqual(SUB_QQ_Q(RationalNumber(-1, 4), RationalNumber(1, 4)).__str__(),
                         RationalNumber(-1, 2).__str__())

    def test_MUL_QQ_Q(self):
        self.assertRaises(TypeError, MUL_QQ_Q, NaturalNumber(2), NaturalNumber(3))
        self.assertRaises(TypeError, MUL_QQ_Q, Integer(3), Integer(5))
        self.assertRaises(TypeError, MUL_QQ_Q, 1.0, 5)
        self.assertRaises(TypeError, MUL_QQ_Q, '10', 's')
        self.assertRaises(TypeError, MUL_QQ_Q, RationalNumber(3, 2), 's')
        self.assertEqual(MUL_QQ_Q(RationalNumber(2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(1, 1).__str__())
        self.assertEqual(MUL_QQ_Q(RationalNumber(-2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(-1, 1).__str__())
        self.assertEqual(MUL_QQ_Q(RationalNumber(0, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(0, 2).__str__())
        self.assertEqual(MUL_QQ_Q(RationalNumber(2, 1), RationalNumber(-3, 2)).__str__(),
                         RationalNumber(-3, 1).__str__())

    def test_DIV_QQ_Q(self):
        self.assertRaises(TypeError, DIV_QQ_Q, NaturalNumber(2), NaturalNumber(3))
        self.assertRaises(TypeError, DIV_QQ_Q, Integer(3), Integer(5))
        self.assertRaises(TypeError, DIV_QQ_Q, 1.0, 5)
        self.assertRaises(TypeError, DIV_QQ_Q, '10', 's')
        self.assertRaises(TypeError, DIV_QQ_Q, RationalNumber(3, 2), 's')
        self.assertEqual(DIV_QQ_Q(RationalNumber(2, 1), RationalNumber(1, 2)).__str__(),
                         RationalNumber(4, 1).__str__())
        self.assertEqual(DIV_QQ_Q(RationalNumber(2, 1), RationalNumber(2, 1)).__str__(),
                         RationalNumber(1, 1).__str__())
        self.assertEqual(DIV_QQ_Q(RationalNumber(-1, 2), RationalNumber(2, 1)).__str__(),
                         RationalNumber(-1, 4).__str__())
        self.assertEqual(DIV_QQ_Q(RationalNumber(-2, 1), RationalNumber(2, 1)).__str__(),
                         RationalNumber(-1, 1).__str__())


def main():
    unittest.main()


if __name__ == "__main__":
    main()
