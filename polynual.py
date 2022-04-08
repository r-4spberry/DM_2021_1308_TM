import math
from typing import List
import rational
import natnum
from rational import ADD_QQ_Q
from rational import SUB_QQ_Q
from rational import MUL_QQ_Q
from rational import DIV_QQ_Q
from natnum import nat_lcm
from natnum import nat_gcd
from integer import TRANS_Z_N
from integer import TRANS_N_Z
from integer import ABS_Z_N
from integer import DIV_ZZ_Z
import copy
from rational import RationalNumber
class Polynom:
    def __init__(self, coef: List[rational.RationalNumber]):
        """
        Возвращает многочлен в стандартном виде (ax^n+...+yx^1+z)
        принимает массив чисел типа RationalNumbers

        выполнил: Мельник Даниил
        """
        if coef is None:
            coef = []
        self.coef = coef
    def __str__(self):
        s = ""
        for i in range(len(self.coef)-1, 0, -1):
            s += f"{self.coef[i]}x^{i}+"
        if (len(self.coef)!=0):
            s += str(self.coef[0])
        return s
    def __repr__(self):
        return f"Polynom({repr(self.coef)})"
    
    def remove_leading_zeros(self):
        while self.coef[-1].numer == 0 and len(self.coef) > 1:
            self.coef.pop()

def ADD_PP_P(p1, p2):
    """
    складывает два многочлена типа Polynom
    принимает на вход два массива одинаковой длины р1 и р2 (малый дополняется нулевыми коэффициентами до длины большого)
    """
    p3 = Polynom([])
    
    if len(p1.coef) < len(p2.coef):
        p1 = copy.deepcopy(p2)
        p2 = copy.deepcopy(p1)
    else:
        p1 = copy.deepcopy(p1)
        p2 = copy.deepcopy(p2)
        
    while len(p2.coef) < len(p1.coef):
        p2.coef.append(RationalNumber(0, 1))
        
    for i in range (len(p1.coef)):
        k=ADD_QQ_Q(p1.coef[i],p2.coef[i])
        p3.coef.append(k)
    
    p3.remove_leading_zeros()
    return p3

def SUB_PP_P(p1, p2):
    """
    вычитает один многочлен из другого
    принимает на вход два массива одинаковой длины р1 и р2 (малый дополняется нулевыми коэффициентами до длины большого)
    возвращает многочлен типа Polynom
    """
    p3=Polynom([])
    p1r=copy.deepcopy(p1)
    p2r=copy.deepcopy(p2)
    for i in range (0,len(p1r.coef)):
        if (i<len(p2r.coef)):
            k=SUB_QQ_Q(p1r.coef[i],p2r.coef[i])
            p3.coef.append(k)
    
    p3.remove_leading_zeros()
    return p3

def MUL_PQ_P (p1,x):
    """
    умножает многочлен р1 в нормальном виде (при старшем коэффициенте стоит не ноль) на число х типа RationalNumbers
    """
    p3=copy.deepcopy(p1)
    for i in range(0,len(p1.coef)):
        p3.coef[i] = rational.MUL_QQ_Q(p1.coef[i], x)
    
    p3.remove_leading_zeros()
    return p3

def MUL_Pxk_P (p1,k):
    """
    умножает многочлен p1 в нормальном виде на переменную в степени k
    возвращает многочлен с новыми степенями, при старых степенях стоят нули
    """
    p3=copy.deepcopy(p1)
    p3.coef.reverse()
    for i in range(k):
        p3.coef.append(rational.RationalNumber(0,1))
    p3.coef.reverse()
    
    p3.remove_leading_zeros()
    return p3

def LED_P_Q(p1):
    """
    возвращает старший коэффициент в формате RationalNumbers многочлена р1 в нормальном виде
    """
    p1r=copy.deepcopy(p1)
    return p1r.coef[len(p1r.coef)-1]

def DEG_P_N (p1):
    """
    возвращает степень многочлена p1 (в нормальном виде)
    """
    p1r=copy.deepcopy(p1)
    return len(p1r.coef)-1

def FAC_P_Q(p1):
    """
    принимает на вход многочлен р1 в нормальном виде
    выносит из многочлена НОК числителей и НОД знаменателей коэффициентов
    возвращает вынесенное число (Р) формата RationalNumbers и многочлен р3
    """
    p3=Polynom([])
    p1=copy.deepcopy(p1)
    p2=Polynom([])
    p4=Polynom([])
    p3.coef=p1.coef
    p2.coef=p1.coef
    znam=[]
    chisl=[]
    k=natnum.NaturalNumber
    for i in range(len(p3.coef)):
        chisl.append(p3.coef[i].numer)
        znam.append(p3.coef[i].denom)

    while (len(znam)!=1):
        k=nat_gcd(znam[0],znam[1])
        for i in range(2):
            znam.pop(0)
        znam.insert(0,k)

    while (len(chisl)!=1):
        k=nat_lcm(chisl[0],chisl[1])
        for i in range(2):
            chisl.pop(0)
        chisl.insert(0,k)
    nzn=znam[0]
    nch=chisl[0]
    P=RationalNumber(str(nch),str(nzn))
    for i in range (len(p1.coef)):
        d=DIV_QQ_Q(p1.coef[i],P)
        p4.coef.append(d)
        
    p4.remove_leading_zeros()
    return P, p4

def MUL_PP_P(pP,pA): #"""принимает многочлены одинаковой длины"""
    """
    принимает на вход многочлены одинаковой длины pP и pА
    возвращает многочлен - результат
    """
    pP=copy.deepcopy(pP)
    pA=copy.deepcopy(pA)
    P4=Polynom([])
    deg=2*(len(pP.coef)-1)
    for i in range (deg+1):
        P4.coef.append(RationalNumber('0','1'))
    for i in range(0, len(pP.coef)):
        if(i<len(pA.coef)):
            P1 = MUL_Pxk_P(pP, i)
            P2 = MUL_PQ_P(P1, pA.coef[i])
            P2r=copy.deepcopy(P2)
            P4= ADD_PP_P(P2r,P4)
    
    P4.remove_leading_zeros()
    return P4

def DIV_PP_P (pP,pA):
    """
    выполняет деление многочленов
    возвращает целое от деления
    """
    pP = copy.deepcopy(pP)
    pA = copy.deepcopy(pA)
    P3=copy.deepcopy(pP)
    m=DEG_P_N(pP)
    n=DEG_P_N(pA)
    Pres=Polynom([])
    print('m== ', m)
    print('n== ', n)
    while(m>=n):
        P1=MUL_Pxk_P(pA,m-n)
        k = DIV_QQ_Q(P3.coef[len(P3.coef)-1],P1.coef[len(P1.coef)-1])
        P2=MUL_PQ_P(P1,k)
        P3=SUB_PP_P(P3,P2)
        P3.coef.pop(len(P3.coef)-1)
        m=DEG_P_N(P3)
        Pres.coef.append(k)
    Pres.coef.reverse()
    
    Pres.remove_leading_zeros()
    return Pres

def MOD_PP_P (pP,pA):
    """
    выполняет деление многочленов
    возвращает остаток от деления
    """
    pP = copy.deepcopy(pP)
    pA = copy.deepcopy(pA)
    n=DEG_P_N(pA)-1
    pP=copy.deepcopy(pP)
    pA=copy.deepcopy(pA)
    Pres=DIV_PP_P(pP, pA)
    Pr=MUL_PP_P(pA,Pres)
    result=SUB_PP_P(pP,Pr)
    m=DEG_P_N(result)
    result.coef.reverse()
    for i in range(m-n):
        result.coef.pop(0)
    result.coef.reverse()
    
    result.remove_leading_zeros()
    return result

def GCF_PP_P (p1, p2):
    """
    находит НОД двух многочленов
    возвращает многочлен
    """
    P1=copy.deepcopy(p1)
    P2=copy.deepcopy(p2)
    m=1
    res=Polynom([])
    while (m!=0):
        if (DEG_P_N(P1)>DEG_P_N(P2)):
            P1=MOD_PP_P(P1, P2)
        if (DEG_P_N(P2)>DEG_P_N(P1)):
            P2=MOD_PP_P(P2, P1)
        m=min(DEG_P_N(P2),DEG_P_N(P1))
    g=max(DEG_P_N(P2),DEG_P_N(P1))
    if (DEG_P_N(P1)==g):
        res=P1
    else:
        res=P2
        
    res.remove_leading_zeros()
    return res

def DER_P_P (p1):
    """
    возвращает производную многочлена
    """
    P1=copy.deepcopy(p1)
    Res=Polynom([])
    for i in range(DEG_P_N(P1)+1):
        m=len(P1.coef)-i-1
        k=rational.RationalNumber(str(m),'1')
        h=MUL_QQ_Q(P1.coef[i],k)
        Res.coef.append(h)
    Res.coef.pop(len(Res.coef)-1)
    
    Res.remove_leading_zeros()
    return Res

def NMR_P_P(poly):
    """Преобразование многочлена — кратные корни в простые
    --Заглушка--
    Возвращает многочлен с сокращенными кратными корнями
    """
    return Polynom([RationalNumber(1), RationalNumber(0), RationalNumber(1)])



def main():
    p2 = Polynom([rational.RationalNumber(-2), rational.RationalNumber(1)])
    p1 = Polynom([rational.RationalNumber(-1), rational.RationalNumber(1)])
    p  = MUL_PP_P(p1, p1)
    p  = MUL_PP_P(p, p1)
    p  = MUL_PP_P(p, p2)
    p  = MUL_PP_P(p, p2)
    
    print(p) 

    P1=DER_P_P(p1)
    print(P1)
    #print(p1.coef[0], p1.coef[1])
    #print(p2.coef[0], p2.coef[1], p2.coef[2])
    #print(p1)
    #print(type(a))
    #P1, P2, P3 = MUL_PP_P(p2,p1)
    #print(P1,'\n',P2,'\n',P3)
    #input()


if __name__ == "__main__":
    main()

