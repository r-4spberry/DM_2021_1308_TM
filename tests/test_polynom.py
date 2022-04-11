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

        # ---1--- стандартные многочлены разных длин 1
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(4, 1), rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(3, 1)])
        pres1=Polynom([RationalNumber(3,1), RationalNumber(7,1), RationalNumber(6,1)])
        self.assertEqual(ADD_PP_P(p1,p2).__str__(),pres1.__str__())

        #---2--- стандартные многочлены разных длин 2
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(4, 1), rational.RationalNumber(6, 1)])
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(3, 1), RationalNumber(7, 1), RationalNumber(6, 1)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3--- стандартный многочлен с многочленом из одного элемента
        p2 = Polynom([rational.RationalNumber(4, 1), rational.RationalNumber(5, 1),
                      rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(8, 1)])
        p1 = Polynom([rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(7,1), RationalNumber(5,1), RationalNumber(6,1), RationalNumber(7,1), RationalNumber(8,1)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---4--- стандартный многочлен с многоленом с пропуском 1
        p2 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(5, 1), rational.RationalNumber(6, 1)])
        p1 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(2,1), RationalNumber(1,1), RationalNumber(5,1), RationalNumber(8,1)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---5--- стандартный многочлен с многоленом с пропуском 2
        p1 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(5, 1), rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(2, 1), RationalNumber(1, 1), RationalNumber(5, 1), RationalNumber(8, 1)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---6--- стандартные многочлеы
        p1 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(2, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([rational.RationalNumber(2, 1),
                         rational.RationalNumber(3, 1), rational.RationalNumber(3, 1)])
        self.assertEqual(ADD_PP_P(p1, p2).__str__(), pres1.__str__())



    def test_SUB_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- стандартные многочлены разных длин 1
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(4, 1), rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(-1,1), RationalNumber(1,1), RationalNumber(6,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---2--- стандартные многочлены разных длин 2
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(4, 1), rational.RationalNumber(6, 1)])
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(1,1), RationalNumber(-1,1), RationalNumber(-6,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3--- стандартный многочлен с многочленом из одного элемента
        p1 = Polynom([rational.RationalNumber(4, 1), rational.RationalNumber(5, 1),
                      rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(8, 1)])
        p2 = Polynom([rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(1,1), RationalNumber(5,1), RationalNumber(6,1), RationalNumber(7,1), RationalNumber(8,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4--- стандартный многочлен с многоленом с пропуском 1
        p1 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(5, 1), rational.RationalNumber(6, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(1,1), RationalNumber(5,1), RationalNumber(4,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---5--- стандартный многочлен с многоленом с пропуском 2
        p2 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(5, 1), rational.RationalNumber(6, 1)])
        p1 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(-1,1), RationalNumber(-5,1), RationalNumber(-4,1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---6--- стандартные многочлеы
        p1 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([rational.RationalNumber(0, 1),
                      rational.RationalNumber(1, 1), rational.RationalNumber(-1, 1)])
        self.assertEqual(SUB_PP_P(p1, p2).__str__(), pres1.__str__())


    def test_MUL_PQ_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- стандартный многочлен
        p1 = Polynom([rational.RationalNumber(1, 1),
                   rational.RationalNumber(1, 1), rational.RationalNumber(2, 1), rational.RationalNumber(3, 1)])
        x=RationalNumber(4,1)
        pres1 = Polynom([RationalNumber(4,1), RationalNumber(4,1), RationalNumber(8,1), RationalNumber(12,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())

        # ---2--- стандартный многочлен с дробями
        p1 = Polynom([rational.RationalNumber(1, 3),
                      rational.RationalNumber(8, 27), rational.RationalNumber(2, 1)])
        x = RationalNumber(3, 1)
        pres1 = Polynom([RationalNumber(1,1), RationalNumber(8,9), RationalNumber(6,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())


        # ---3--- многочлен с промежутком
        p1 = Polynom([rational.RationalNumber(9, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(3, 1)])
        x = RationalNumber(1, 3)
        pres1 = Polynom([RationalNumber(3,1), RationalNumber(0,3), RationalNumber(0,3), RationalNumber(0,3), RationalNumber(1,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())


        # ---4--- многочлен из одного элемента, умножение обратных
        p1 = Polynom([rational.RationalNumber(2, 1)])
        x = RationalNumber(1, 2)
        pres1 = Polynom([RationalNumber(1,1)])
        self.assertEqual(MUL_PQ_P(p1, x).__str__(), pres1.__str__())


    def test_MUL_Pxk_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- многочлен с одним членом
        p1 = Polynom([rational.RationalNumber(2, 1)])
        x=2
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(2,1)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())

        # ---2--- многочлен с пропуском
        p1 = Polynom([rational.RationalNumber(1, 1),rational.RationalNumber(0, 1),rational.RationalNumber(1, 1)])
        x = 3
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(0,1), RationalNumber(1,1), RationalNumber(0,1), RationalNumber(1,1)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())

        # ---3--- стандартный многочлен
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(1, 1), rational.RationalNumber(7, 9),
                      rational.RationalNumber(2, 1), rational.RationalNumber(1, 3)])
        x = 1
        pres1 = Polynom([rational.RationalNumber(0,1),rational.RationalNumber(2, 1), rational.RationalNumber(1, 1), rational.RationalNumber(7, 9),
                      rational.RationalNumber(2, 1), rational.RationalNumber(1, 3)])
        self.assertEqual(MUL_Pxk_P(p1, x).__str__(), pres1.__str__())


    def test_LED_P_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- многочлен из одного элемента
        p1 = Polynom([rational.RationalNumber(7, 3)])
        pres1 = RationalNumber(7,3)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))

        # ---2--- многочлен с большим пропуском
        p1 = Polynom([rational.RationalNumber(8, 1),rational.RationalNumber(0, 1),rational.RationalNumber(0, 1),
                      rational.RationalNumber(0, 1),rational.RationalNumber(3, 1)])
        pres1 = RationalNumber(3, 1)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))

        # ---3--- многочлен с маленикими пропусками
        p1 = Polynom([rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(1, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(3, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = RationalNumber(2, 1)
        self.assertEqual(str(LED_P_Q(p1)), str(pres1))


        # ---4---


    def test_DEG_P_N(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- стандартный многочлен
        p1 = Polynom([rational.RationalNumber(3, 5), rational.RationalNumber(12, 1), rational.RationalNumber(32, 1)])
        pres1 = 2
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

        # ---2--- многочлен с пропуском
        p1 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = 4
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

        # ---3--- многочлен из одного элемента
        p1 = Polynom([rational.RationalNumber(3, 1)])
        pres1 = 0
        self.assertEqual(str(DEG_P_N(p1)), str(pres1))

    def test_FAC_P_Q(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- стандартный многочлен
        p1 = Polynom([rational.RationalNumber(1, 4),rational.RationalNumber(2, 16),rational.RationalNumber(7, 8)])
        pres1 = RationalNumber(1,16)
        pres2 = Polynom([RationalNumber(4,1), RationalNumber(2,1), RationalNumber(14,1)])
        p,P=FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

        # ---2--- многочлен с хотя бы одним целым коэффициентом
        p1 = Polynom([rational.RationalNumber(1, 2),rational.RationalNumber(3, 4),rational.RationalNumber(2, 1),rational.RationalNumber(5, 8)])
        pres1 = RationalNumber(1, 8)
        pres2 = Polynom([RationalNumber(4,1), RationalNumber(6,1), RationalNumber(16,1), RationalNumber(5,1)])
        p, P = FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

        # ---3--- многочлен с хотя бы одним целым коэффициентом
        p1 = Polynom([rational.RationalNumber(8, 5), rational.RationalNumber(4, 2),
                      rational.RationalNumber(2, 3)])
        pres1 = RationalNumber(2, 30)
        pres2 = Polynom([RationalNumber(24,1), RationalNumber(30,1), RationalNumber(10,1)])
        p, P = FAC_P_Q(p1)
        self.assertEqual(str(P), str(pres2))
        self.assertEqual(str(p), str(pres1))

        # многочленыы, в которых есть хотя бы один нулевой коэффициент не рассматриваются,
        # так как вынесение нуля из числителя равносильно делению на ноль всего коэффициента

    def test_MUL_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- многочлены разных длин 1
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(2,1), RationalNumber(4,1), RationalNumber(3,1), RationalNumber(1,1)])
        self.assertEqual(MUL_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2--- многочлены разных длин 2
        p2 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(2, 1), RationalNumber(4, 1), RationalNumber(3, 1), RationalNumber(1, 1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())


        # ---3--- стандартный многочлен на многочлен из одного элемента 1
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(4,1), RationalNumber(4,1), RationalNumber(2,1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4--- оба многочлена с пропусками
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(8, 1),rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(16,1), RationalNumber(2,1), RationalNumber(0,1), RationalNumber(8,1), RationalNumber(1,1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---5--- стандартный многочлен на многочлен с одним элементом-перемнной в степени
        p1 = Polynom([rational.RationalNumber(8, 1), rational.RationalNumber(1, 1), rational.RationalNumber(2, 1),
                      rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(0,1), RationalNumber(8,1), RationalNumber(1,1), RationalNumber(2,1), RationalNumber(1,1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---6--- многочлены с единственными элементами-переменными в степени, разной длины
        p1 = Polynom([rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(0, 1), RationalNumber(0, 1), RationalNumber(0, 1), RationalNumber(0, 1),
                         RationalNumber(0, 1), RationalNumber(1, 1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---7--- стандартные многочлены одинаковых длин 1
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(4, 1), rational.RationalNumber(3, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(4, 1), RationalNumber(7, 1), RationalNumber(9, 1),
                         RationalNumber(5, 1), RationalNumber(2, 1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---8--- стандартные многочлены одинаковых длин 2
        p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(4, 1), rational.RationalNumber(3, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(4, 1), RationalNumber(7, 1), RationalNumber(9, 1),
                         RationalNumber(5, 1), RationalNumber(2, 1)])
        self.assertEqual(MUL_PP_P(p1, p2).__str__(), pres1.__str__())


    def test_DIV_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- большей длины на меньшей с разными знаками у коэффициентов
        p1 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(-8, 1), rational.RationalNumber(7, 1),
                      rational.RationalNumber(2, 1)])
        p2 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(-14,1), RationalNumber(3,1), RationalNumber(2,1)])
        self.assertEqual(DIV_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2--- меньшей длины на большей с разными знаками у коэффициентов (ноль)
        p2 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(-8, 1), rational.RationalNumber(7, 1),
                      rational.RationalNumber(2, 1)])
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(0,1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3--- одинаковой длины 1
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1,1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4--- одинаковой длины 2
        p2 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1, 1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4--- одинаковые
        p2 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1, 1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---5--- кратные (в ответе дробь)
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(14, 1), rational.RationalNumber(16, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(1,2)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---6--- кратные (в ответе целое)
        p2 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(14, 1), rational.RationalNumber(16, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(2, 1)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---7--- стандартный многочлен на одинарный с переменной (в ответе дробные коэффициенты)
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1),
                      rational.RationalNumber(5, 1)])
        p2 = Polynom([rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(1,2), RationalNumber(5,2)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---8--- стандартный многочлен на одинарный с константой (в ответе дробные коэффициенты)
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1),
                      rational.RationalNumber(5, 1)])
        p2 = Polynom([ rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(7,2), RationalNumber(4,1), RationalNumber(1,2), RationalNumber(5,2)])
        self.assertEqual(DIV_PP_P(p1, p2).__str__(), pres1.__str__())


    def test_MOD_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- одинаковой длины 1 (в остатке переменные)
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1,1), RationalNumber(1,1)])
        self.assertEqual(MOD_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2--- одинаковой длины 2 (в остатке переменные)
        p2 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(-1, 1), RationalNumber(-1, 1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3--- большей длины на меньшей с разными знаками у коэффициентов
        p1 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(-8, 1), rational.RationalNumber(7, 1),
                      rational.RationalNumber(2, 1)])
        p2 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(31, 1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4--- меньшей длины на большей с разными знаками у коэффициентов (само делимое)
        p2 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(-8, 1), rational.RationalNumber(7, 1),
                      rational.RationalNumber(2, 1)])
        p1 = Polynom([rational.RationalNumber(2, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(2,1), RationalNumber(1,1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---5--- стандартный многочлен на одинарный с переменной
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1),
                      rational.RationalNumber(5, 1)])
        p2 = Polynom([rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(7,1), RationalNumber(8,1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---6--- стандартный многочлен на одинарный с константой (при этом получается отсутсвие остатка)
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1),
                      rational.RationalNumber(5, 1)])
        p2 = Polynom([rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(0,1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---7--- кратные 1 (нулевой остаток)
        p1 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p2 = Polynom([rational.RationalNumber(14, 1), rational.RationalNumber(16, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(0,1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---8--- кратные 2 (нулевой остаток)
        p2 = Polynom([rational.RationalNumber(7, 1), rational.RationalNumber(8, 1), rational.RationalNumber(1, 1)])
        p1 = Polynom([rational.RationalNumber(14, 1), rational.RationalNumber(16, 1), rational.RationalNumber(2, 1)])
        pres1 = Polynom([RationalNumber(0, 1)])
        self.assertEqual(MOD_PP_P(p1, p2).__str__(), pres1.__str__())

    def test_GCF_PP_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- сначала большая степень потом меньшая
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1),
                                             rational.RationalNumber(6, 1)])
        p2= Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 1), rational.RationalNumber(3, 1)])
        pres1 = Polynom([RationalNumber(1,1)])
        self.assertEqual(GCF_PP_P(p1,p2).__str__(),pres1.__str__())

        # ---2--- сначала меньшая степень потом большая
        p2 = Polynom([rational.RationalNumber(8, 1), rational.RationalNumber(2, 1), rational.RationalNumber(7, 1),
                      rational.RationalNumber(8, 1)])
        p1 = Polynom([rational.RationalNumber(9, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1,1)])
        self.assertEqual(GCF_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---3--- один из многочленов с пропусками
        p1 = Polynom([rational.RationalNumber(8, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(8, 1)])
        p2 = Polynom([rational.RationalNumber(9, 1), rational.RationalNumber(1, 1), rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1,1)])
        self.assertEqual(GCF_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---4--- один из многочленов - единица 1
        p1 = Polynom([rational.RationalNumber(8, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(8, 1)])
        p2 = Polynom([rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1, 1)])
        self.assertEqual(GCF_PP_P(p1, p2).__str__(), pres1.__str__())

        # ---5--- один из многочленов - единица 1
        p2 = Polynom([rational.RationalNumber(8, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(8, 1)])
        p1 = Polynom([rational.RationalNumber(1, 1)])
        pres1 = Polynom([RationalNumber(1, 1)])
        self.assertEqual(GCF_PP_P(p1, p2).__str__(), pres1.__str__())

    def test_DER_P_P(self):
        self.assertRaises(TypeError, NaturalNumber(2))
        self.assertRaises(TypeError, Integer(3))
        self.assertRaises(TypeError, 1.0)
        self.assertRaises(TypeError, 1)
        self.assertRaises(TypeError, '10')
        self.assertRaises(TypeError, (NaturalNumber(2), NaturalNumber(9)))
        self.assertRaises(TypeError, [1, 2, 3])

        # ---1--- стандартный многочлен с целыми коэффициентами
        p1 = Polynom([rational.RationalNumber(3, 1), rational.RationalNumber(1, 3),
                      rational.RationalNumber(6, 3)])
        pres1 = Polynom([RationalNumber(1,3), RationalNumber(4,1)])
        self.assertEqual(DER_P_P(p1).__str__(),pres1.__str__())

        # ---2--- многочлен с дробными коэффициентами, которые должны сократиться
        p1 = Polynom([rational.RationalNumber(81, 1), rational.RationalNumber(1, 3),
                      rational.RationalNumber(1, 2)])
        pres1 = Polynom([RationalNumber(1, 3), RationalNumber(1, 1)])
        self.assertEqual(DER_P_P(p1).__str__(), pres1.__str__())


        # ---3--- большой многочлен с разными коэффициентами (дробные и целые)
        p1 = Polynom([rational.RationalNumber(99, 1), rational.RationalNumber(1, 1),
                      rational.RationalNumber(1, 8), rational.RationalNumber(3, 1), rational.RationalNumber(9, 16), rational.RationalNumber(1, 1),
                    rational.RationalNumber(1, 36), rational.RationalNumber(2, 7)])

        pres1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(1, 4), rational.RationalNumber(9, 1),
                         rational.RationalNumber(9, 4), rational.RationalNumber(5, 1),
                    rational.RationalNumber(1, 6), rational.RationalNumber(2, 1)])
        self.assertEqual(DER_P_P(p1).__str__(), pres1.__str__())

        # ---4--- многочлен с пропусками
        p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(0, 1),
                      rational.RationalNumber(7, 2)])
        pres1 = Polynom([RationalNumber(0,1), RationalNumber(7,1)])
        self.assertEqual(DER_P_P(p1).__str__(), pres1.__str__())




def main():
    unittest.main()


if __name__ == "__main__":
    main()
2