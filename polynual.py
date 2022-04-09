from typing import List
import rational
import natnum
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
    
    def normalise(self):
        while len(self.coef) > 1 and self.coef[-1].numer == 0:
            self.coef.pop()
        if len(self.coef) == 0:
            self.coef = [RationalNumber(0)]
            
def ADD_PP_P(p1, p2):
    """
    складывает два многочлена типа Polynom
    принимает на вход два массива одинаковой длины р1 и р2 (малый дополняется нулевыми коэффициентами до длины большого)
    """
    p3 = Polynom([])
    p2r=copy.deepcopy(p2)
    p1r=copy.deepcopy(p1)
    if (len(p2r.coef)<len(p1r.coef)):
        for i in range(len(p1r.coef)-len(p2r.coef)):
            p2r.coef.append(rational.RationalNumber('0','1'))
    if (len(p1r.coef)<len(p2r.coef)):
        for i in range(len(p2r.coef)-len(p1r.coef)):
            p1r.coef.append(rational.RationalNumber('0','1'))
    #print('p11=', p1r.__str__())
    #print('p21=', p2r.__str__())

    for i in range (len(p1r.coef)):
        k=rational.ADD_QQ_Q(p1r.coef[i],p2r.coef[i])
        p3.coef.append(k)
    return p3

def SUB_PP_P(p1, p2):
    """
    вычитает один многочлен из другого
    принимает на вход два многочлена р1 и р2 (малый дополняется нулевыми коэффициентами до длины большого)
    возвращает многочлен типа Polynom
    """
    p3=Polynom([])
    p1r=copy.deepcopy(p1)
    p2r=copy.deepcopy(p2)
    if (len(p2r.coef)<len(p1r.coef)):
        for i in range(len(p1r.coef)-len(p2r.coef)):
            p2r.coef.append(rational.RationalNumber('0','1'))
    if (len(p1r.coef)<len(p2r.coef)):
        for i in range(len(p2r.coef)-len(p1r.coef)):
            p1r.coef.append(rational.RationalNumber('0','1'))
    if (len(p2r.coef) < len(p1r.coef)):
        p2r.coef.reverse()
        for i in range(len(p1r.coef) - len(p2r.coef)):
            p2r.coef.append(rational.RationalNumber('0', '1'))
        p2r.coef.reverse()
    if (len(p1r.coef) < len(p2r.coef)):
        p1r.coef.reverse()
        for i in range(len(p2r.coef) - len(p1r.coef)):
            p1r.coef.append(rational.RationalNumber('0', '1'))
        p1r.coef.reverse()
    for i in range (0,len(p1r.coef)):
        if (i<len(p2r.coef)):
            k=rational.SUB_QQ_Q(p1r.coef[i],p2r.coef[i])
            p3.coef.append(k)
    return p3

def MUL_PQ_P (p1,x):
    """
    умножает многочлен р1 в нормальном виде (при старшем коэффициенте стоит не ноль) на число х типа RationalNumbers
    """
    p3=copy.deepcopy(p1)
    for i in range(0,len(p1.coef)):
        p3.coef[i] = rational.MUL_QQ_Q(p1.coef[i], x)
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
        k=natnum.nat_lcm(znam[0],znam[1])
        for i in range(2):
            znam.pop(0)
        znam.insert(0,k)

    while (len(chisl)!=1):
        k=natnum.nat_gcd(chisl[0],chisl[1])
        for i in range(2):
            chisl.pop(0)
        chisl.insert(0,k)
    nzn=znam[0]
    nch=chisl[0]
    P=rational.RationalNumber(str(nch),str(nzn))
    for i in range (len(p1.coef)):
        d=rational.DIV_QQ_Q(p1.coef[i],P)
        p4.coef.append(d)
    return P, p4

def MUL_PP_P(pP,pA): #"""принимает многочлены одинаковой длины"""
    """
    принимает на вход многочлены одинаковой длины pP и pА
    возвращает многочлен - результат
    """
    pP=copy.deepcopy(pP)
    pA=copy.deepcopy(pA)

    if (len(pP.coef)<len(pA.coef)):

        for i in range(len(pA.coef)-len(pP.coef)):
            pP.coef.append(RationalNumber('0','1'))

    if (len(pA.coef)<len(pP.coef)):
        for i in range(len(pP.coef)-len(pA.coef)):
            pA.coef.append(RationalNumber('0','1'))

    P4=Polynom([])
    deg=2*(len(pP.coef)-1)
    for i in range (deg+1):
        P4.coef.append(RationalNumber('0','1'))
    for i in range(0, len(pP.coef)):
        if(i<len(pA.coef)):
            P1 = MUL_Pxk_P(pP, i)
            P2 = MUL_PQ_P(P1, pA.coef[i])
            P2r=copy.deepcopy(P2)
            for j in range (deg+1-len(P2.coef)):
                P2r.coef.append(RationalNumber('0','1'))
            P4= ADD_PP_P(P2r,P4)
    P4.normalise()
    return P4

def divmod(p1, p2):
    """
    Возвращает целое и остаток от деления двух многочленов
    """
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)

    if DEG_P_N(p1) >= DEG_P_N(p2):
        diff = DEG_P_N(p1) - DEG_P_N(p2)
        p2.coef = [RationalNumber()]*diff + p2.coef
    else:
        return Polynom([RationalNumber()]), p1

    ans = Polynom([])
    d = p2.coef[-1]
    
    for i in range(diff+1):
        m = rational.DIV_QQ_Q(p1.coef[-1], d)
        ans.coef = [m] + ans.coef
        p1 = SUB_PP_P(p1, MUL_PP_P(p2,Polynom([m])))
        p1.coef.pop()
        p2.coef.pop(0)
        
    ans.normalise()
    p1.normalise()
    
    return ans, p1

def DIV_PP_P (p1,p2):
    """
    возвращает целое от деления двух многочленов
    """
    return divmod(p1, p2)[0]



def MOD_PP_P (p1,p2):
    """
    возвращает остаток от деления двух многочленов
    """
    return divmod(p1, p2)[1]

def GCF_PP_P (p1, p2):
    """
    находит НОД двух многочленов
    возвращает многочлен
    """
    P1=copy.deepcopy(p1)
    P2=copy.deepcopy(p2)
    m=1
    while True:
        P2 = MUL_PQ_P(P2, rational.DIV_QQ_Q(RationalNumber(1), P2.coef[0]))
        P1 = MUL_PQ_P(P1, rational.DIV_QQ_Q(RationalNumber(1), P1.coef[0]))
        if (DEG_P_N(P1)>DEG_P_N(P2)):
            P1=MOD_PP_P(P1, P2)
            if DEG_P_N(P1) == 0 and P1.coef[0].numer == 0:
                return P2
        else:
            P2=MOD_PP_P(P2, P1)
            if DEG_P_N(P2) == 0 and P2.coef[0].numer == 0:
                return P1


def DER_P_P (p1):
    """
    возвращает производную многочлена
    """
    P1=copy.deepcopy(p1)
    Res=Polynom([])
    f=len(P1.coef)-1
    m=len(P1.coef)-1
    for i in range (len(P1.coef)):
        k=f-i
        h=rational.MUL_QQ_Q(P1.coef[m], rational.RationalNumber(str(k),'1'))
        Res.coef.append(h)
        m -= 1
    Res.coef.pop(len(Res.coef)-1)
    Res.coef.reverse()

    return Res

def NMR_P_P(p):
    """
    Возвращает многочлен с сокращенными кратными корнями
    """
    q = DER_P_P(p)
    d = GCF_PP_P(p, q)
    ans = DIV_PP_P(p, d)
    return ans

def main():

    p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(3, 1), rational.RationalNumber(6, 1), rational.RationalNumber(7, 1), rational.RationalNumber(3, 1)])
    p2 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(3, 1), rational.RationalNumber(3, 1), rational.RationalNumber(1, 1)])
    print(p1)
    print(p2)
    print(GCF_PP_P(p1, p2))
    
if __name__ == "__main__":
    main()

